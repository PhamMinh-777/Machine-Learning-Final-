# ==============================================================================
# File: src/models/lstm.py
# Nhiệm vụ: Kiến trúc LSTM
# ==============================================================================
"""
MÔ TẢ CHI TIẾT NHIỆM VỤ:
1. Xây dựng mạng hồi quy Long Short-Term Memory (LSTM):
   - Học các mối tương quan phụ thuộc thời gian dài hạn (Long-term Temporal Dependencies) trong dữ liệu chuỗi giá.
   - Giải quyết vấn đề triệt tiêu đạo hàm (Vanishing Gradient) của RNN truyền thống.
2. Thành phần kiến trúc dự kiến:
   - LSTM Layers (Stacked LSTM 1-3 lớp, bidirectional hoặc unidirectional).
   - Dropout giữa các tầng LSTM để chống overfitting.
   - Fully Connected Layer phân loại ở output bước thời gian cuối cùng (Last Hidden State).

CÁC LỚP DỰ KIẾN HIỆN THỰC (TODO):
- class StockLSTM(nn.Module):
  + __init__(self, input_dim: int, hidden_dim: int, num_layers: int, output_dim: int = 1, dropout: float = 0.2)
  + forward(self, x: torch.Tensor) -> torch.Tensor
"""

# Lưu ý: Chưa viết mã thực thi, file này chỉ định nghĩa cấu trúc và nhiệm vụ.
