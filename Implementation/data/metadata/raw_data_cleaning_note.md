# Ghi chú xử lý dữ liệu OHLC thô

- Ngày xử lý: 2026-11-26.
- Dữ liệu nguồn trong `data/raw/` được giữ nguyên.
- Tạo bản đã xử lý trong `data/processed/raw_cleaned/` (mỗi mã và `all_stocks.csv`).
- Chỉ loại dòng có quan hệ OHLC không hợp lệ: `High < max(Open, Close)`, `Low > min(Open, Close)`, hoặc `High < Low`.
- Không điền median và không loại các dòng vì missing value; lần kiểm tra này không phát hiện ô thiếu.
- Đã loại 30 dòng trên 71.679 dòng (còn 71.649): 28 mã vào 2021-11-02; ACB.VN vào 2025-06-04 và 2025-06-05.
- Danh sách đầy đủ các dòng bị loại nằm trong `excluded_ohlc_rows.csv`; báo cáo kiểm tra dữ liệu nguồn nằm trong `raw_data_quality_report.csv`.
- Khi tạo cửa sổ chuỗi thời gian, cần lưu ý những phiên bị loại tạo khoảng trống trong chuỗi. Bản raw được giữ lại để có thể đối chiếu hoặc tái tạo dữ liệu đã xử lý.
