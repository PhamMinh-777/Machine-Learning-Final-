# KẾ HOẠCH TRIỂN KHAI DỰ ÁN (PROJECT PLAN)
## Dự án: Final-ML-Stock-Prediction (Question 2)

---

## Giai đoạn 1: Chuẩn bị môi trường & Thu thập dữ liệu
- [x] Thiết lập cấu trúc thư mục chuẩn và các module Python trong `src/`.
- [x] Tạo file cấu hình trung tâm `configs/config.yaml`.
- [x] Xác định danh sách thư viện cần thiết trong `requirements.txt`.
- [ ] Thu thập dữ liệu chứng khoán (OHLCV) lưu vào `data/raw/`.
- [ ] Kiểm tra dữ liệu và phân tích sơ bộ (EDA).

---

## Giai đoạn 2: Tiền xử lý & Trích xuất đặc trưng kỹ thuật
- [ ] Xử lý dữ liệu thiếu, kiểm tra các phiên không giao dịch (`src/preprocessing.py`).
- [ ] Tính toán các chỉ báo kỹ thuật: SMA, EMA, MACD, RSI, Bollinger Bands, ATR (`src/features.py`).
- [ ] Tạo nhãn xu hướng giá và áp dụng cửa sổ trượt Sliding Window (`src/dataset.py`).
- [ ] Chuẩn hóa dữ liệu bằng Scaler và lưu scaler vào `artifacts/scalers/`.
- [ ] Đóng gói PyTorch Dataset & DataLoader (`src/dataset.py`).

---

## Giai đoạn 3: Huấn luyện mô hình cơ sở & Machine Learning truyền thống
- [ ] Hiện thực mô hình Baseline: Majority Class & Persistence (`src/models/baseline.py`).
- [ ] Huấn luyện các mô hình Machine Learning truyền thống: Logistic Regression, Random Forest, XGBoost (`src/models/traditional.py`).
- [ ] Đánh giá kết quả ban đầu và lưu kết quả vào `results/metrics/`.

---

## Giai đoạn 4: Hiện thực và huấn luyện các mô hình Deep Learning
- [ ] Xây dựng mô hình 1D-CNN (`src/models/cnn.py`).
- [ ] Xây dựng mô hình LSTM (`src/models/lstm.py`).
- [ ] Xây dựng mô hình lai Hybrid CNN-LSTM (`src/models/cnn_lstm.py`).
- [ ] Xây dựng mô hình nâng cao CNN-LSTM-Attention (`src/models/cnn_lstm_attention.py`).
- [ ] Hoàn thiện vòng lặp huấn luyện, Early Stopping và lưu Checkpoints (`src/trainer.py`).
- [ ] Huấn luyện và tinh chỉnh siêu tham số trên từng kiến trúc.

---

## Giai đoạn 5: Đánh giá, Trực quan hóa & Hoàn thiện báo cáo
- [ ] Đánh giá toàn diện các mô hình với Accuracy, Precision, Recall, F1-Score, ROC-AUC (`src/evaluator.py`).
- [ ] Vẽ Learning Curves, Confusion Matrix và biểu đồ so sánh (`src/visualization.py`).
- [ ] Phân tích trọng số Attention Weights và phân tích sai số (Error Analysis).
- [ ] Tích hợp toàn bộ luồng tương tác vào `notebooks/FinalML_Question2.ipynb`.
- [ ] Hoàn thiện báo cáo chi tiết trong `docs/FINAL_REPORT.docx`.
