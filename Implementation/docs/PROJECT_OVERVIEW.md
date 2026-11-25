# TÀI LIỆU TỔNG QUAN DỰ ÁN VÀ NHIỆM VỤ CÁC FILE
## Project: Final-ML-Stock-Prediction

---

## 1. Mục tiêu dự án
Dự án nhằm giải quyết bài toán dự đoán xu hướng giá chứng khoán dựa trên chuỗi thời gian dữ liệu lịch sử OHLCV (Open - High - Low - Close - Volume) và các chỉ báo phân tích kỹ thuật. Dự án xây dựng một pipeline hoàn chỉnh từ thu thập, tiền xử lý, trích xuất đặc trưng, huấn luyện và so sánh đa dạng mô hình:
- **Baseline Models:** Majority Class, Persistence Baseline.
- **Traditional Machine Learning:** Logistic Regression, Random Forest, XGBoost.
- **Deep Learning Architectures:** 1D-CNN, LSTM, Hybrid CNN-LSTM, CNN-LSTM-Attention.

---

## 2. Bảng phân công nhiệm vụ chi tiết của từng file

### 2.1. Nhóm xử lý dữ liệu (Data Processing - `src/`)
| File | Nhiệm vụ chi tiết |
| :--- | :--- |
| **`src/data_loader.py`** | • Thu thập và đọc dữ liệu OHLCV từ file CSV/Excel cục bộ hoặc API trực tuyến (`yfinance`, `vnstock`).<br>• Kiểm tra schema dữ liệu (các cột giá, ngày tháng, kiểu dữ liệu datetime).<br>• Sắp xếp theo thứ tự thời gian. |
| **`src/preprocessing.py`** | • Xử lý dữ liệu thiếu (Missing values: ffill, bfill) và ngoại lai.<br>• Chuẩn hóa dữ liệu (MinMaxScaler, StandardScaler) đảm bảo không bị Data Leakage.<br>• Phân chia tập dữ liệu theo thứ tự thời gian (Time-series Train / Validation / Test Split). |
| **`src/features.py`** | • Tính toán các chỉ báo kỹ thuật xu hướng: SMA, EMA, MACD.<br>• Tính toán các chỉ báo động lượng: RSI, Stochastic.<br>• Tính toán các chỉ báo biến động & khối lượng: ATR, Bollinger Bands, Volume MA.<br>• Tạo các đặc trưng trễ (Lag features) và tỷ suất sinh lời. |
| **`src/dataset.py`** | • Tạo nhãn mục tiêu (Label Engineering: Tăng [1] / Giảm [0]).<br>• Biến đổi chuỗi thời gian sang dạng cửa sổ trượt (Sliding Window / Lookback Window).<br>• Xây dựng lớp `StockDataset` kế thừa PyTorch `Dataset` và đóng gói thành `DataLoader`. |

---

### 2.2. Nhóm mô hình học máy & học sâu (Model Implementation - `src/models/`)
| File | Nhiệm vụ chi tiết |
| :--- | :--- |
| **`src/models/baseline.py`** | • **Majority Class:** Dự đoán nhãn có tần suất xuất hiện cao nhất trong tập train.<br>• **Persistence Baseline:** Dự đoán giá/xu hướng tiếp theo giữ nguyên theo phiên gần nhất. Làm mốc chuẩn đối sánh cơ sở. |
| **`src/models/traditional.py`** | • Xây dựng mô hình máy học truyền thống: **Logistic Regression**, **Random Forest**, **XGBoost**.<br>• Cung cấp giao diện huấn luyện, dự đoán xác suất và trích xuất độ quan trọng của đặc trưng (Feature Importance). |
| **`src/models/cnn.py`** | • Kiến trúc **1D-CNN** nhằm trích xuất các đặc trưng không gian cục bộ (Local spatial patterns) và mẫu hình giá ngắn hạn từ dữ liệu chuỗi thời gian. |
| **`src/models/lstm.py`** | • Kiến trúc **LSTM (Long Short-Term Memory)** để nắm bắt sự phụ thuộc thời gian dài hạn (Long-term temporal dependencies) trong chuỗi giá. |
| **`src/models/cnn_lstm.py`** | • Kiến trúc lai **Hybrid CNN-LSTM**: Tầng CNN đóng vai trò trích xuất đặc trưng bậc cao, sau đó chuyển sang LSTM để học diễn tiến thời gian. |
| **`src/models/cnn_lstm_attention.py`** | • Kiến trúc nâng cao **CNN-LSTM kết hợp Attention Mechanism**: Tính trọng số chú ý cho từng mốc thời gian quan trọng, nâng cao độ chính xác và tính giải thích được (Explainability). |

---

### 2.3. Nhóm huấn luyện, đánh giá & trực quan hóa (Training & Evaluation - `src/`)
| File | Nhiệm vụ chi tiết |
| :--- | :--- |
| **`src/trainer.py`** | • Quản lý vòng lặp huấn luyện (Training Loop) và đánh giá trên tập kiểm định (Validation Loop).<br>• Cấu hình Optimizer (Adam, AdamW, SGD) và Learning Rate Scheduler.<br>• Triển khai cơ chế **Early Stopping** chống overfitting và tự động lưu **Checkpoint** tốt nhất. |
| **`src/evaluator.py`** | • Đánh giá hiệu năng với đầy đủ các chỉ số: **Accuracy, Precision, Recall, F1-score, ROC-AUC**.<br>• Tạo và phân tích ma trận nhầm lẫn (Confusion Matrix).<br>• Tổng hợp và so sánh hiệu năng giữa tất cả các mô hình thành bảng báo cáo. |
| **`src/visualization.py`** | • Vẽ đồ thị quá trình học (**Learning Curves**: Train Loss vs Val Loss, Accuracy).<br>• Vẽ Heatmap cho **Confusion Matrix**.<br>• Vẽ biểu đồ cột so sánh hiệu năng giữa các mô hình.<br>• Vẽ trọng số **Attention Weights** và biểu đồ phân tích sai số (Error Analysis). |
| **`src/utils.py`** | • Thiết lập cố định **Random Seed** (Python, NumPy, PyTorch) đảm bảo tính tái lập (Reproducibility).<br>• Nhận diện thiết bị tính toán phần cứng (**Device**: CUDA GPU / MPS / CPU).<br>• Đọc file cấu hình `configs/config.yaml`.<br>• Các hàm hỗ trợ lưu/đọc checkpoints và ghi logs. |

---

### 2.4. File cấu hình & Notebook tương tác
| File | Nhiệm vụ chi tiết |
| :--- | :--- |
| **`configs/config.yaml`** | • Trung tâm quản lý toàn bộ tham số của dự án: đường dẫn dữ liệu, thông số chỉ báo kỹ thuật, kích thước cửa sổ trượt (lookback window), siêu tham số mô hình (layers, hidden_dim, learning_rate, batch_size, epochs...). |
| **`notebooks/FinalML_Question2.ipynb`** | • Notebook chính thực hiện toàn bộ luồng nghiên cứu và thử nghiệm (Interactive Pipeline).<br>• Nhập cấu hình, gọi trực tiếp các module trong `src/` để chạy EDA, huấn luyện, đánh giá và xuất báo cáo trực quan. |

---

### 2.5. Cấu trúc lưu trữ dữ liệu & kết quả (Data Storage)
| Thư mục | Nội dung lưu trữ |
| :--- | :--- |
| **`data/raw/`** | Dữ liệu gốc thu thập từ nguồn (chưa qua xử lý). |
| **`data/processed/`** | Dữ liệu đã làm sạch, xử lý khuyết thiếu và gắn nhãn. |
| **`artifacts/models/`** | File lưu trọng số mô hình đã huấn luyện (`.pt`, `.pkl`). |
| **`artifacts/scalers/`** | Bộ chuẩn hóa dữ liệu (`MinMaxScaler.pkl`, `StandardScaler.pkl`). |
| **`results/figures/`** | Các đồ thị, biểu đồ trực quan hóa xuất ra để phục vụ viết báo cáo. |
| **`results/predictions/`** | Kết quả dự đoán chi tiết trên tập test của các mô hình. |
| **`results/metrics/`** | File tổng hợp chỉ số đánh giá (CSV/JSON/Markdown). |
| **`docs/`** | Tài liệu dự án (`PROJECT_OVERVIEW.md`, `PLAN.md`, `FINAL_REPORT.docx`). |
