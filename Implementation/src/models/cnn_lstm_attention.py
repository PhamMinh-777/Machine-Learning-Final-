# ==============================================================================
# File: src/models/cnn_lstm_attention.py
# Nhiệm vụ: Kiến trúc CNN-LSTM-Attention
# ==============================================================================
"""
MÔ TẢ CHI TIẾT NHIỆM VỤ:
1. Xây dựng mô hình nâng cao CNN-LSTM kết hợp cơ chế Attention (Temporal / Feature Attention):
   - CNN: Trích xuất đặc trưng hình thái giá và biến động cục bộ.
   - LSTM: Mã hóa thông tin theo dòng thời gian thành chuỗi hidden states.
   - Attention Mechanism: Tính trọng số chú ý (Attention Weights) cho từng thời điểm trong chuỗi.
     Cho phép mô hình tập trung vào các ngày giao dịch quan trọng (ví dụ: ngày có biến động đột biến, break out).
   - Classifier: Đầu ra dự đoán phân loại xu hướng từ vector tổng hợp (Context Vector).
2. Trích xuất trọng số Attention Weights để trực quan hóa và phân tích tính giải thích được (Explainability).

CÁC LỚP DỰ KIẾN HIỆN THỰC (TODO):
- class TemporalAttention(nn.Module):
  + __init__(self, hidden_dim: int)
  + forward(self, lstm_output: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]
- class StockCNNLSTMAttention(nn.Module):
  + __init__(self, input_dim: int, cnn_out_channels: int, lstm_hidden_dim: int, num_classes: int = 1, dropout: float = 0.2)
  + forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]  # Output logits và attention weights
"""

# Lưu ý: Chưa viết mã thực thi, file này chỉ định nghĩa cấu trúc và nhiệm vụ.
