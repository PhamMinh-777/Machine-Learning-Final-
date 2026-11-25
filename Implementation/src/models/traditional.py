# ==============================================================================
# File: src/models/traditional.py
# Nhiệm vụ: Logistic Regression, Random Forest, XGBoost
# ==============================================================================
"""
MÔ TẢ CHI TIẾT NHIỆM VỤ:
1. Triển khai các thuật toán Machine Learning truyền thống phân loại xu hướng giá chứng khoán:
   - Logistic Regression: Mô hình tuyến tính phân loại làm mốc cơ bản cho ML.
   - Random Forest: Ensemble cây quyết định với cơ chế Bagging, xử lý tốt phi tuyến.
   - XGBoost (hoặc LightGBM): Gradient Boosting mạnh mẽ cho dữ liệu dạng bảng và đặc trưng kỹ thuật.
2. Hỗ trợ chuẩn hóa dữ liệu đầu vào (flattened sequence hoặc feature summary vector).
3. Cung cấp API thống nhất (fit, predict, predict_proba, save_model, load_model) tương thích với sklearn.

CÁC HÀM VÀ LỚP DỰ KIẾN HIỆN THỰC (TODO):
- get_traditional_models(config: dict) -> dict[str, Any]
- class TraditionalMLPipeline
  + train(model_name: str, X_train, y_train)
  + evaluate(model_name: str, X_test, y_test)
  + get_feature_importances(model_name: str)
"""

# Lưu ý: Chưa viết mã thực thi, file này chỉ định nghĩa cấu trúc và nhiệm vụ.
