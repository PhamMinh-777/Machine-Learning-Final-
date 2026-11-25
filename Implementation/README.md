# Final-ML-Stock-Prediction

Dự án Machine Learning & Deep Learning dự đoán xu hướng giá chứng khoán (Stock Price & Trend Prediction) sử dụng dữ liệu lịch sử OHLCV kết hợp các chỉ báo phân tích kỹ thuật và so sánh giữa các kiến trúc Baseline, Machine Learning truyền thống và Deep Learning (1D-CNN, LSTM, CNN-LSTM, CNN-LSTM-Attention).

---

## 📁 Cấu trúc thư mục dự án

```text
Final-ML-Stock-Prediction/
│
├── 📁 data/
│   ├── raw/                        # Dữ liệu gốc chưa xử lý
│   └── processed/                  # Dữ liệu đã làm sạch & tiền xử lý
│
├── 📁 notebooks/
│   └── FinalML_Question2.ipynb     # Notebook tích hợp thực thi toàn bộ pipeline
│
├── 📁 src/
│   ├── __init__.py
│   ├── data_loader.py              # Thu thập và đọc dữ liệu OHLCV
│   ├── preprocessing.py            # Xử lý dữ liệu thiếu, chuẩn hóa, chia dữ liệu
│   ├── features.py                 # Tính RSI, MACD, SMA, EMA, ATR và các chỉ báo
│   ├── dataset.py                  # Tạo nhãn, Sliding Window, PyTorch Dataset
│   │
│   ├── 📁 models/
│   │   ├── __init__.py
│   │   ├── baseline.py             # Majority Class, Persistence Baseline
│   │   ├── traditional.py          # Logistic Regression, Random Forest, XGBoost
│   │   ├── cnn.py                  # Kiến trúc 1D CNN
│   │   ├── lstm.py                 # Kiến trúc LSTM
│   │   ├── cnn_lstm.py             # Kiến trúc Hybrid CNN-LSTM
│   │   └── cnn_lstm_attention.py   # Kiến trúc CNN-LSTM-Attention
│   │
│   ├── trainer.py                  # Training Loop, Validation, Early Stopping, Checkpoints
│   ├── evaluator.py                # Accuracy, Precision, Recall, F1-score, Confusion Matrix
│   ├── visualization.py            # Learning Curves, biểu đồ so sánh, phân tích sai số
│   └── utils.py                    # Random Seed, Device, các hàm tiện ích
│
├── 📁 configs/
│   └── config.yaml                 # Quản lý thông số toàn bộ dự án
│
├── 📁 artifacts/
│   ├── models/                     # Mô hình đã huấn luyện (.pt, .pkl)
│   └── scalers/                    # Bộ chuẩn hóa đã fit (.pkl)
│
├── 📁 results/
│   ├── figures/                    # Biểu đồ sử dụng trong báo cáo
│   ├── predictions/                # Kết quả dự đoán
│   └── metrics/                    # Kết quả đánh giá và so sánh
│
├── 📁 tests/                       # Unit tests kiểm tra tính đúng đắn
│
├── 📁 docs/
│   ├── PROJECT_OVERVIEW.md         # Tài liệu chi tiết nhiệm vụ và kiến trúc
│   ├── PLAN.md                     # Kế hoạch thực hiện từng giai đoạn
│   └── FINAL_REPORT.docx           # Báo cáo tổng kết đồ án
│
├── requirements.txt                # Danh sách thư viện cần thiết
├── README.md                       # Hướng dẫn tổng quan
└── .gitignore                      # Cấu hình bỏ qua file nhị phân & dữ liệu nặng
```

---

## 🚀 Hướng dẫn cài đặt môi trường

1. **Tạo môi trường ảo (Virtual Environment):**
   ```bash
   python -m venv .venv
   # Kích hoạt trên Windows:
   .venv\Scripts\activate
   # Kích hoạt trên Linux/macOS:
   source .venv/bin/activate
   ```

2. **Cài đặt các thư viện cần thiết:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Khởi chạy Jupyter Notebook:**
   ```bash
   jupyter notebook notebooks/FinalML_Question2.ipynb
   ```

Xem chi tiết nhiệm vụ từng module tại [docs/PROJECT_OVERVIEW.md](file:///C:/TDTU%202024-2028/Ch%C3%ADnh%20th%E1%BB%A9c/N%C4%83m%203/ML/Final-ML-Stock-Prediction/docs/PROJECT_OVERVIEW.md).
