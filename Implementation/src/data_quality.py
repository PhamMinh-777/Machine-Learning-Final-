"""Quality checks for downloaded raw OHLCV CSV files."""

from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = ("Open", "High", "Low", "Close", "Volume")
NUMERIC_COLUMNS = (*REQUIRED_COLUMNS,)


def _invalid_ohlc_mask(df: pd.DataFrame) -> pd.Series:
    values = df[list(NUMERIC_COLUMNS)].apply(pd.to_numeric, errors="coerce")
    return (
        (values["High"] < values[["Open", "Close"]].max(axis=1))
        | (values["Low"] > values[["Open", "Close"]].min(axis=1))
        | (values["High"] < values["Low"])
    ).fillna(False)


def clean_raw_data(
    raw_dir: str | Path,
    output_dir: str | Path,
    exclusion_log: str | Path,
) -> tuple[pd.DataFrame, int]:
    """Write clean copies, excluding rows with invalid OHLC relationships.

    Raw inputs are never modified. Per-ticker files are the source for the
    cleaned combined file, so a bad row is recorded exactly once.
    """
    raw_dir, output_dir = Path(raw_dir), Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    ticker_files = sorted(p for p in raw_dir.glob("*.csv") if p.name != "all_stocks.csv")
    if not ticker_files:
        raise FileNotFoundError(f"No per-ticker CSV files found in {raw_dir}")

    clean_frames, exclusions = [], []
    for path in ticker_files:
        df = pd.read_csv(path)
        required = {"Date", *REQUIRED_COLUMNS}
        missing = required - set(df.columns)
        if missing:
            raise ValueError(f"{path.name} is missing columns: {sorted(missing)}")
        if "Ticker" not in df.columns:
            df["Ticker"] = path.stem

        invalid = _invalid_ohlc_mask(df)
        removed = df.loc[invalid].copy()
        if not removed.empty:
            removed["source_file"] = path.name
            removed["reason"] = "Invalid OHLC: High < max(Open, Close) or Low > min(Open, Close) or High < Low"
            exclusions.append(removed)

        clean = df.loc[~invalid].copy()
        clean["Date"] = pd.to_datetime(clean["Date"], errors="raise")
        clean = clean.sort_values("Date").reset_index(drop=True)
        clean["Date"] = clean["Date"].dt.strftime("%Y-%m-%d")
        clean.to_csv(output_dir / path.name, index=False)
        clean_frames.append(clean)

    combined = pd.concat(clean_frames, ignore_index=True).sort_values(["Ticker", "Date"]).reset_index(drop=True)
    combined.to_csv(output_dir / "all_stocks.csv", index=False)

    exclusion_df = pd.concat(exclusions, ignore_index=True) if exclusions else pd.DataFrame()
    log_path = Path(exclusion_log)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    exclusion_df.to_csv(log_path, index=False)
    return combined, len(exclusion_df)


def inspect_raw_csv(path: str | Path) -> dict:
    """Inspect one raw CSV and return a compact, serializable quality summary."""
    path = Path(path)
    result = {
        "file": path.name,
        "rows": 0,
        "columns_ok": False,
        "date_parse_errors": 0,
        "missing_cells": 0,
        "duplicate_dates": 0,
        "out_of_order_rows": 0,
        "non_numeric_cells": 0,
        "non_positive_prices": 0,
        "negative_volume": 0,
        "invalid_ohlc_rows": 0,
        "start_date": "",
        "end_date": "",
        "status": "",
        "issues": "",
    }
    issues = []
    try:
        df = pd.read_csv(path)
    except Exception as exc:
        result.update(status="ERROR", issues=f"CSV read failed: {exc}")
        return result

    result["rows"] = len(df)
    required = {"Date", *REQUIRED_COLUMNS}
    missing_columns = sorted(required - set(df.columns))
    result["columns_ok"] = not missing_columns
    if missing_columns:
        issues.append("missing columns: " + ", ".join(missing_columns))
        result.update(status="ERROR", issues="; ".join(issues))
        return result
    if df.empty:
        result.update(status="ERROR", issues="empty file")
        return result

    result["missing_cells"] = int(df[list(required)].isna().sum().sum())
    dates = pd.to_datetime(df["Date"], errors="coerce")
    result["date_parse_errors"] = int(dates.isna().sum())
    valid_dates = dates.dropna()
    if not valid_dates.empty:
        result["start_date"] = valid_dates.min().date().isoformat()
        result["end_date"] = valid_dates.max().date().isoformat()
        keys = pd.DataFrame({"Date": dates})
        if "Ticker" in df.columns:
            keys["Ticker"] = df["Ticker"]
            result["out_of_order_rows"] = int(
                keys.assign(Date=dates).groupby("Ticker", sort=False)["Date"]
                .apply(lambda series: int((series.diff().dropna() < pd.Timedelta(0)).sum())).sum()
            )
        else:
            result["out_of_order_rows"] = int((valid_dates.diff().dropna() < pd.Timedelta(0)).sum())
        result["duplicate_dates"] = int(keys.duplicated().sum())

    values = df[list(NUMERIC_COLUMNS)].apply(pd.to_numeric, errors="coerce")
    result["non_numeric_cells"] = int((values.isna() & df[list(NUMERIC_COLUMNS)].notna()).sum().sum())
    result["non_positive_prices"] = int((values[["Open", "High", "Low", "Close"]] <= 0).any(axis=1).sum())
    result["negative_volume"] = int((values["Volume"] < 0).sum())
    result["invalid_ohlc_rows"] = int(
        ((values["High"] < values[["Open", "Close"]].max(axis=1))
         | (values["Low"] > values[["Open", "Close"]].min(axis=1))
         | (values["High"] < values["Low"])).sum()
    )

    checks = (
        ("date_parse_errors", "invalid dates"),
        ("missing_cells", "missing values"),
        ("duplicate_dates", "duplicate date keys"),
        ("out_of_order_rows", "rows out of date order"),
        ("non_numeric_cells", "non-numeric OHLCV values"),
        ("non_positive_prices", "non-positive prices"),
        ("negative_volume", "negative volume"),
        ("invalid_ohlc_rows", "invalid OHLC relationships"),
    )
    issues.extend(f"{result[key]} {label}" for key, label in checks if result[key])
    result["status"] = "PASS" if not issues else "CHECK"
    result["issues"] = "; ".join(issues)
    return result


def audit_raw_data(data_dir: str | Path, output_path: str | Path | None = None) -> pd.DataFrame:
    """Inspect all CSVs in a raw-data directory and optionally save the report."""
    data_dir = Path(data_dir)
    paths = sorted(data_dir.glob("*.csv"))
    if not paths:
        raise FileNotFoundError(f"No CSV files found in {data_dir}")
    report = pd.DataFrame(inspect_raw_csv(path) for path in paths)
    if output_path is not None:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        report.to_csv(output_path, index=False)
    return report


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    report_path = root / "data" / "metadata" / "raw_data_quality_report.csv"
    report = audit_raw_data(root / "data" / "raw", report_path)
    print(report.to_string(index=False))
    print(f"\nSaved report: {report_path}")
    cleaned_dir = root / "data" / "processed" / "raw_cleaned"
    exclusion_path = root / "data" / "metadata" / "excluded_ohlc_rows.csv"
    combined, removed = clean_raw_data(root / "data" / "raw", cleaned_dir, exclusion_path)
    print(f"Cleaned rows: {len(combined)}; excluded rows: {removed}")
    print(f"Cleaned data: {cleaned_dir}")
    print(f"Exclusion log: {exclusion_path}")
