# ==============================================================================
# File: src/dataset.py
# Nhiệm vụ: Tạo nhãn, Sliding Window, PyTorch Dataset
# ==============================================================================
"""
MÔ TẢ CHI TIẾT NHIỆM VỤ:
1. Định nghĩa bài toán dự đoán và tạo nhãn (Label Engineering):
   - Bài toán phân loại xu hướng: Tăng (1) vs Giảm/Đi ngang (0) cho phiên tiếp theo (t + 1) hoặc t + k.
   - Bài toán hồi quy (nếu mở rộng): Dự đoán giá trị Close hoặc tỷ suất sinh lời tương lai.
2. Phương pháp cửa sổ trượt (Sliding Window / Rolling Window):
   - Biến đổi dữ liệu chuỗi thời gian 2D thành tensor 3D: (Samples, Lookback_window, Features).
   - Ví dụ: Dùng thông tin 30 ngày qua (T = 30) để dự đoán xu hướng ngày thứ 31.
3. Xây dựng lớp PyTorch Dataset & DataLoader:
   - Kế thừa torch.utils.data.Dataset cho việc nạp dữ liệu theo batch.
   - Tạo DataLoader cho Train, Validation và Test với các tùy chọn batch_size, shuffle (False cho sequence).

CÁC LỚP VÀ HÀM DỰ KIẾN HIỆN THỰC (TODO):
- create_classification_labels(df: pd.DataFrame, horizon: int = 1, threshold: float = 0.0) -> pd.DataFrame
- create_sliding_windows(data: np.ndarray, labels: np.ndarray, window_size: int) -> Tuple[np.ndarray, np.ndarray]
- class StockDataset(torch.utils.data.Dataset)
- get_dataloaders(train_data, val_data, test_data, batch_size: int) -> Tuple[DataLoader, DataLoader, DataLoader]
"""

# Lưu ý: Chưa viết mã thực thi, file này chỉ định nghĩa cấu trúc và nhiệm vụ.
