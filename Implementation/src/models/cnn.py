# ==============================================================================
# File: src/models/cnn.py
# Nhiệm vụ: Kiến trúc 1D CNN
# ==============================================================================
"""
MÔ TẢ CHI TIẾT NHIỆM VỤ:
1. Xây dựng mạng nơ-ron tích chập 1 chiều (1D Convolutional Neural Network - 1D CNN):
   - Trích xuất các mẫu hình cục bộ (Local Patterns) và hình thái giá (Chart Patterns) từ chuỗi thời gian OHLCV.
2. Thành phần kiến trúc dự kiến:
   - Conv1d layers (với kernel size phù hợp, e.g., 3, 5).
   - Batch Normalization / Layer Normalization giúp ổn định quá trình huấn luyện.
   - Activation function (ReLU / LeakyReLU / GELU).
   - MaxPool1d hoặc AdaptiveAvgPool1d để giảm chiều không gian.
   - Dropout giảm hiện tượng overfitting.
   - Fully Connected Layers (Linear) đầu ra phân loại xác suất xu hướng (Sigmoid/Softmax).

CÁC LỚP DỰ KIẾN HIỆN THỰC (TODO):
- class StockCNN1D(nn.Module):
  + __init__(self, input_dim: int, seq_len: int, num_classes: int = 1, dropout: float = 0.2)
  + forward(self, x: torch.Tensor) -> torch.Tensor
"""

# Lưu ý: Chưa viết mã thực thi, file này chỉ định nghĩa cấu trúc và nhiệm vụ.
