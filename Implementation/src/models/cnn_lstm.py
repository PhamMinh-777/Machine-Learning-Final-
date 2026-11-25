# ==============================================================================
# File: src/models/cnn_lstm.py
# Nhiệm vụ: Kiến trúc Hybrid CNN-LSTM
# ==============================================================================
"""
MÔ TẢ CHI TIẾT NHIỆM VỤ:
1. Xây dựng mô hình kết hợp lai ghép Hybrid CNN-LSTM:
   - Giai đoạn 1 (CNN Feature Extractor): 1D-CNN trích xuất các đặc trưng không gian cục bộ từ dữ liệu giá và chỉ báo kỹ thuật.
   - Giai đoạn 2 (LSTM Temporal Processor): Dòng đặc trưng sau CNN được đưa vào mạng LSTM để học quan hệ chuỗi theo thời gian.
   - Giai đoạn 3 (Dense Classifier): Tầng fully-connected kết hợp đưa ra xác suất dự đoán xu hướng.
2. Lợi thế: Kết hợp khả năng trích xuất mẫu biểu đồ của CNN và khả năng ghi nhớ dài hạn của LSTM.

CÁC LỚP DỰ KIẾN HIỆN THỰC (TODO):
- class StockCNNLSTM(nn.Module):
  + __init__(self, input_dim: int, cnn_out_channels: int, lstm_hidden_dim: int, num_classes: int = 1, dropout: float = 0.2)
  + forward(self, x: torch.Tensor) -> torch.Tensor
"""

# Lưu ý: Chưa viết mã thực thi, file này chỉ định nghĩa cấu trúc và nhiệm vụ.
