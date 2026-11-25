# ==============================================================================
# File: src/data_loader.py
# Nhiệm vụ: Thu thập và đọc dữ liệu OHLCV
# ==============================================================================
"""
MÔ TẢ CHI TIẾT NHIỆM VỤ:
1. Đọc dữ liệu chứng khoán lịch sử (Open, High, Low, Close, Volume - OHLCV) từ các nguồn:
   - File cục bộ (CSV, Excel, Parquet) lưu tại `data/raw/`.
   - Thu thập trực tuyến qua các thư viện tài chính (ví dụ: yfinance).
2. Kiểm tra tính toàn vẹn và định dạng dữ liệu (Schema validation):
   - Đảm bảo cột Date/Time được chuyển sang datetime index chuẩn.
   - Sắp xếp dữ liệu theo thứ tự thời gian tăng dần.
   - Kiểm tra các cột bắt buộc: Open, High, Low, Close, Volume.
3. Lưu dữ liệu đã nạp sơ bộ vào thư mục chỉ định hoặc truyền sang pipeline tiền xử lý.

CÁC HÀM HIỆN THỰC:
- validate_ohlcv_schema(df: pd.DataFrame) -> bool
- load_csv_data(filepath: str | Path) -> pd.DataFrame
- fetch_online_stock_data(ticker: str, start_date: str, end_date: str, ...) -> pd.DataFrame
- download_stock(ticker: str) -> pd.DataFrame
- download_all_stocks() -> pd.DataFrame
"""

import os
import sys
import time
import shutil
import tempfile
from pathlib import Path
import certifi
import pandas as pd


# ------------------------------------------------------------------------------
# Khắc phục lỗi libcurl/yfinance trên Windows khi đường dẫn chứa ký tự tiếng Việt
# (SSLError: curl (77) error adding trust anchors from locations)
# ------------------------------------------------------------------------------
def _fix_curl_ssl_cert():
    try:
        ca_path = certifi.where()
        need_fix = False
        try:
            ca_path.encode('ascii')
        except UnicodeEncodeError:
            need_fix = True

        if need_fix or " " in ca_path:
            temp_dir = tempfile.gettempdir()
            try:
                temp_dir.encode('ascii')
            except UnicodeEncodeError:
                temp_dir = os.environ.get("SystemRoot", "C:\\Windows") + "\\Temp"

            safe_ca_path = os.path.join(temp_dir, "cacert.pem")
            if not os.path.exists(safe_ca_path) or os.path.getsize(safe_ca_path) != os.path.getsize(ca_path):
                shutil.copyfile(ca_path, safe_ca_path)
            os.environ["CURL_CA_BUNDLE"] = safe_ca_path
            os.environ["SSL_CERT_FILE"] = safe_ca_path
    except Exception:
        pass


_fix_curl_ssl_cert()

# Import yfinance sau khi đã cấu hình biến môi trường SSL
import yfinance as yf

# Đảm bảo đường dẫn import hoạt động khi chạy từ mọi thư mục
_current_dir = Path(__file__).resolve().parent
_project_root = _current_dir.parent
if str(_current_dir) not in sys.path:
    sys.path.insert(0, str(_current_dir))
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

try:
    from .config import (
        load_config,
        get_tickers,
        get_project_path,
    )
except ImportError:
    from config import (
        load_config,
        get_tickers,
        get_project_path,
    )


config = load_config()
data_config = config["data"]
download_config = config["download"]
TICKERS = get_tickers(config)
RAW_DIR = get_project_path(config["paths"]["raw_data"])
METADATA_DIR = get_project_path(config["paths"]["metadata"])


def validate_ohlcv_schema(df: pd.DataFrame) -> bool:
    """
    Kiểm tra tính toàn vẹn và định dạng dữ liệu OHLCV:
    - Kiểm tra DataFrame không rỗng.
    - Kiểm tra các cột bắt buộc: Open, High, Low, Close, Volume.
    - Đảm bảo cột Date tồn tại hoặc index là DatetimeIndex.
    """
    if df is None or df.empty:
        raise ValueError("DataFrame rỗng!")

    required_cols = {"Open", "High", "Low", "Close", "Volume"}
    current_cols = set(df.columns)
    missing = required_cols - current_cols
    if missing:
        raise ValueError(f"Thiếu các cột bắt buộc: {missing}")

    if "Date" in df.columns:
        if not pd.api.types.is_datetime64_any_dtype(df["Date"]):
            try:
                pd.to_datetime(df["Date"])
            except Exception as e:
                raise ValueError(f"Cột 'Date' không đúng định dạng datetime: {e}")
    elif not isinstance(df.index, pd.DatetimeIndex):
        raise ValueError("Dữ liệu cần có cột 'Date' hoặc DatetimeIndex!")

    return True


def load_csv_data(filepath) -> pd.DataFrame:
    """
    Đọc dữ liệu chứng khoán lịch sử từ file CSV, kiểm tra định dạng và chuyển Date sang datetime.
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Không tìm thấy file: {filepath}")

    df = pd.read_csv(path)

    # Chuẩn hóa tên cột ngày nếu cần
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values("Date").reset_index(drop=True)
    elif "Datetime" in df.columns:
        df = df.rename(columns={"Datetime": "Date"})
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values("Date").reset_index(drop=True)

    return df


def fetch_online_stock_data(
    ticker: str,
    start_date: str = None,
    end_date: str = None,
    interval: str = "1d",
    auto_adjust: bool = False
) -> pd.DataFrame:
    """
    Tải dữ liệu chứng khoán trực tuyến từ Yahoo Finance cho một mã cổ phiếu.
    """
    _fix_curl_ssl_cert()

    start = start_date or data_config.get("start_date", "2016-01-01")
    end = end_date or data_config.get("end_date", "2026-01-01")

    df = yf.download(
        tickers=ticker,
        start=start,
        end=end,
        interval=interval,
        auto_adjust=auto_adjust,
        multi_level_index=False,
        progress=download_config.get("progress", False),
        threads=download_config.get("threads", False),
        timeout=download_config.get("timeout", 30)
    )

    if df is None or df.empty:
        raise ValueError(f"No data found: {ticker}")

    # Xử lý trường hợp columns bị đa tầng (MultiIndex)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

    df = df.reset_index()

    if "Datetime" in df.columns and "Date" not in df.columns:
        df = df.rename(columns={"Datetime": "Date"})

    df["Date"] = pd.to_datetime(df["Date"])
    df["Ticker"] = ticker

    df = df.sort_values("Date").reset_index(drop=True)
    validate_ohlcv_schema(df)
    return df


def download_stock(ticker: str) -> pd.DataFrame:
    """
    Tải dữ liệu chứng khoán theo cấu hình trong data.yaml.
    """
    return fetch_online_stock_data(
        ticker=ticker,
        start_date=data_config["start_date"],
        end_date=data_config["end_date"],
        interval=data_config["interval"],
        auto_adjust=data_config["auto_adjust"]
    )


def download_all_stocks():
    """
    Tải về bộ dữ liệu cho tất cả các mã cổ phiếu trong cấu hình,
    lưu từng mã vào data/raw/{ticker}.csv và tổng hợp vào data/raw/all_stocks.csv.
    """
    _fix_curl_ssl_cert()
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    METADATA_DIR.mkdir(parents=True, exist_ok=True)

    all_data = []
    logs = []

    print(f"Bắt đầu tải dữ liệu cho {len(TICKERS)} mã cổ phiếu...")

    for ticker in TICKERS:
        print(f"Downloading {ticker}...")
        try:
            df = download_stock(ticker)

            df.to_csv(
                RAW_DIR / f"{ticker}.csv",
                index=False
            )

            all_data.append(df)

            logs.append({
                "Ticker": ticker,
                "Status": "Success",
                "Rows": len(df),
                "StartDate": df["Date"].min(),
                "EndDate": df["Date"].max(),
                "MissingValues": df.isna().sum().sum(),
                "Error": ""
            })

            print(f"Success: {ticker} ({len(df)} rows)")

        except Exception as error:
            logs.append({
                "Ticker": ticker,
                "Status": "Failed",
                "Rows": 0,
                "StartDate": None,
                "EndDate": None,
                "MissingValues": None,
                "Error": str(error)
            })

            print(f"Failed: {ticker} - {error}")

        delay = download_config.get("delay", 0.5)
        if delay > 0:
            time.sleep(delay)

    log_df = pd.DataFrame(logs)
    log_df.to_csv(
        METADATA_DIR / "download_log.csv",
        index=False
    )

    if not all_data:
        raise RuntimeError("No stocks downloaded")

    combined_df = pd.concat(
        all_data,
        ignore_index=True
    )

    combined_df = combined_df.sort_values(
        ["Ticker", "Date"]
    ).reset_index(drop=True)

    combined_df.to_csv(
        RAW_DIR / "all_stocks.csv",
        index=False
    )

    print("\n" + "=" * 50)
    print("HOÀN THÀNH TẢI DỮ LIỆU!")
    print(f"- Số mã thành công: {len(all_data)}/{len(TICKERS)}")
    print(f"- Tổng số dòng: {len(combined_df)}")
    print(f"- Thư mục lưu: {RAW_DIR}")
    print(f"- File tổng hợp: {RAW_DIR / 'all_stocks.csv'}")
    print(f"- Log trạng thái: {METADATA_DIR / 'download_log.csv'}")
    print("=" * 50)

    return combined_df


if __name__ == "__main__":
    download_all_stocks()
