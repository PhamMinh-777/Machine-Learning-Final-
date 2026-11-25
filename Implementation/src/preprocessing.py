# ==============================================================================
# File: src/preprocessing.py
# Nhiệm vụ: Xử lý dữ liệu thiếu, chuẩn hóa, chia dữ liệu
# ==============================================================================
"""
MÔ TẢ CHI TIẾT NHIỆM VỤ:
1. Xử lý dữ liệu thiếu (Missing Value Handling):
   - Xử lý giá trị NaN, Null do ngày nghỉ giao dịch hoặc lỗi thu thập (Forward fill, Backward fill, Drop).
2. Xử lý ngoại lai (Outliers) và kiểm tra tính liên tục của chuỗi thời gian.
3. Chuẩn hóa dữ liệu (Feature Scaling):
   - Áp dụng MinMaxScaler hoặc StandardScaler riêng cho tập Train và áp dụng lên Val/Test.
   - Tránh Data Leakage (không fit scaler trên toàn bộ dữ liệu trước khi chia).
   - Lưu trữ scaler vào `artifacts/scalers/` để phục vụ suy luận thực tế (Inference).
4. Phân chia tập dữ liệu theo chuỗi thời gian (Time-series Train / Validation / Test Split):
   - Chia theo tỷ lệ thời gian (ví dụ: 70% Train, 15% Val, 15% Test) mà không làm xáo trộn thứ tự (Shuffle=False).

CÁC HÀM DỰ KIẾN HIỆN THỰC (TODO):
- handle_missing_values(df: pd.DataFrame, method: str = 'ffill') -> pd.DataFrame
- split_time_series_data(df: pd.DataFrame, train_ratio: float, val_ratio: float) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]
- fit_transform_scaler(train_df: pd.DataFrame, scaler_type: str = 'minmax', save_path: str = None) -> Tuple[pd.DataFrame, Any]
- transform_scaler(df: pd.DataFrame, scaler: Any) -> pd.DataFrame
"""

# Lưu ý: Chưa viết mã thực thi, file này chỉ định nghĩa cấu trúc và nhiệm vụ.
