# ==============================================================================
# File: src/visualization.py
# Nhiệm vụ: Learning Curves, biểu đồ so sánh, phân tích sai số
# ==============================================================================
"""
MÔ TẢ CHI TIẾT NHIỆM VỤ:
1. Trực quan hóa quá trình huấn luyện:
   - Vẽ Learning Curves (Train Loss vs Validation Loss qua các Epoch).
   - Vẽ đường cong Accuracy/F1-score qua từng Epoch để phát hiện Underfitting / Overfitting.
2. Trực quan hóa kết quả đánh giá mô hình:
   - Vẽ Confusion Matrix Heatmap trực quan.
   - Vẽ đường cong ROC Curves & PR Curves so sánh giữa các mô hình.
   - Vẽ biểu đồ cột (Bar Chart) so sánh Accuracy, F1-Score giữa Baseline, Traditional ML và Deep Learning.
3. Phân tích trực quan sâu:
   - Biểu đồ phân bố trọng số Attention Weights theo chuỗi thời gian (đối với CNN-LSTM-Attention).
   - Biểu đồ phân tích sai số (Error Analysis) theo chuỗi thời gian của giá cổ phiếu.
4. Tự động lưu tất cả biểu đồ chất lượng cao (DPI 300) vào thư mục `results/figures/`.

CÁC HÀM DỰ KIẾN HIỆN THỰC (TODO):
- plot_learning_curves(history: dict, save_path: str = None)
- plot_confusion_matrix(cm: np.ndarray, class_names: list, save_path: str = None)
- plot_model_comparison_bar(metrics_df: pd.DataFrame, metric_name: str, save_path: str = None)
- plot_roc_curves(models_probs: dict, y_true: np.ndarray, save_path: str = None)
- plot_attention_weights(attention_weights: np.ndarray, time_steps: list, save_path: str = None)
"""

# Lưu ý: Chưa viết mã thực thi, file này chỉ định nghĩa cấu trúc và nhiệm vụ.
