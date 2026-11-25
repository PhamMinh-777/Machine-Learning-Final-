# ==============================================================================
# File: src/models/baseline.py
# Nhiệm vụ: Majority Class, Persistence Baseline
# ==============================================================================
"""
MÔ TẢ CHI TIẾT NHIỆM VỤ:
1. Xây dựng mô hình cơ sở Majority Class (Mô hình ngây thơ phân loại):
   - Luôn luôn dự đoán nhãn chiếm đa số trong tập huấn luyện (ví dụ: luôn đoán Tăng hoặc luôn đoán Giảm).
   - Đóng vai trò là mốc chuẩn thấp nhất (Lower Bound) mà bất kỳ mô hình ML/DL nào cũng phải vượt qua.
2. Xây dựng mô hình Persistence Baseline (Naive / Random Walk):
   - Dự đoán xu hướng/giá ngày hôm sau bằng với xu hướng/giá ngày hôm trước (t = t - 1).
3. Đánh giá nhanh hiệu năng baseline để so sánh với các mô hình phức tạp hơn.

CÁC LỚP DỰ KIẾN HIỆN THỰC (TODO):
- class MajorityClassBaseline
  + fit(X, y)
  + predict(X)
- class PersistenceBaseline
  + fit(X, y)
  + predict(X)
"""

# Lưu ý: Chưa viết mã thực thi, file này chỉ định nghĩa cấu trúc và nhiệm vụ.
