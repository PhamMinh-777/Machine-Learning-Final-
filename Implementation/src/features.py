# ==============================================================================
# File: src/features.py
# Nhiệm vụ: Tính RSI, MACD, SMA, EMA, ATR và các chỉ báo
# ==============================================================================
"""
MÔ TẢ CHI TIẾT NHIỆM VỤ:
1. Tính toán các chỉ báo kỹ thuật xu hướng (Trend Indicators):
   - Đường trung bình động đơn giản (SMA - Simple Moving Average, vd: SMA 10, 20, 50).
   - Đường trung bình động hàm mũ (EMA - Exponential Moving Average, vd: EMA 12, 26).
   - MACD (Moving Average Convergence Divergence) & đường tín hiệu (Signal Line).
2. Tính toán các chỉ báo động lượng (Momentum Indicators):
   - RSI (Relative Strength Index).
   - Stochastic Oscillator (%K, %D).
3. Tính toán các chỉ báo biến động (Volatility Indicators):
   - ATR (Average True Range).
   - Bollinger Bands (Upper band, Lower band, Middle band).
4. Tính toán các chỉ báo khối lượng giao dịch (Volume Indicators):
   - OBV (On-Balance Volume), Volume Moving Average.
5. Tạo các đặc trưng trễ (Lag Features) và tỷ suất sinh lời (Log Returns / Percentage Returns).

CÁC HÀM DỰ KIẾN HIỆN THỰC (TODO):
- add_moving_averages(df: pd.DataFrame, windows: list) -> pd.DataFrame
- add_rsi(df: pd.DataFrame, period: int = 14) -> pd.DataFrame
- add_macd(df: pd.DataFrame, fast: int = 12, slow: int = 26, signal: int = 9) -> pd.DataFrame
- add_bollinger_bands(df: pd.DataFrame, period: int = 20, std_dev: int = 2) -> pd.DataFrame
- add_atr(df: pd.DataFrame, period: int = 14) -> pd.DataFrame
- build_all_technical_features(df: pd.DataFrame) -> pd.DataFrame
"""

# Lưu ý: Chưa viết mã thực thi, file này chỉ định nghĩa cấu trúc và nhiệm vụ.
