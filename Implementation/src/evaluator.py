# ==============================================================================
# File: src/evaluator.py
# Nhiệm vụ: Accuracy, Precision, Recall, F1-score, Confusion Matrix
# ==============================================================================
"""
MÔ TẢ CHI TIẾT NHIỆM VỤ:
1. Đánh giá toàn diện hiệu năng của các mô hình phân loại trên tập kiểm thử (Test Set):
   - Đô đo chính xác tổng quan: Accuracy.
   - Độ đo cho bài toán mất cân bằng hoặc chi phí sai số: Precision, Recall, F1-Score (Macro / Weighted).
   - Diện tích dưới đường cong ROC (ROC-AUC) và Precision-Recall Curve (PR-AUC).
2. Tính toán ma trận nhầm lẫn (Confusion Matrix):
   - Xác định True Positive (TP), False Positive (FP), True Negative (TN), False Negative (FN).
3. Xuất bảng tổng hợp so sánh hiệu năng giữa các mô hình (Baseline, Traditional ML, CNN, LSTM, CNN-LSTM, Attention).
4. Lưu trữ kết quả đánh giá (metrics dưới dạng JSON / CSV) vào `results/metrics/`.

CÁC HÀM DỰ KIẾN HIỆN THỰC (TODO):
- compute_classification_metrics(y_true: np.ndarray, y_pred: np.ndarray, y_prob: np.ndarray = None) -> dict
- generate_confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray
- compare_all_models(models_predictions: dict, y_true: np.ndarray) -> pd.DataFrame
- save_metrics_report(metrics_dict: dict, output_path: str)
"""

# Lưu ý: Chưa viết mã thực thi, file này chỉ định nghĩa cấu trúc và nhiệm vụ.
