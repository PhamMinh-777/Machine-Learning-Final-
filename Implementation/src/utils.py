# ==============================================================================
# File: src/utils.py
# Nhiệm vụ: Random Seed, Device, các hàm tiện ích
# ==============================================================================
"""
MÔ TẢ CHI TIẾT NHIỆM VỤ:
1. Đảm bảo tính tái lập kết quả thực nghiệm (Reproducibility):
   - Cố định Random Seed cho Python random, NumPy, PyTorch (CPU & CUDA).
   - Thiết lập deterministic cho cuDNN backend.
2. Quản lý thiết bị tính toán (Device Management):
   - Tự động phát hiện và cấu hình phần cứng: CUDA GPU, Apple Silicon MPS hoặc CPU.
3. Quản lý cấu hình (Configuration Loader):
   - Đọc và phân tích file cấu hình `configs/config.yaml`.
4. Quản lý file và lưu trữ:
   - Tạo tự động các thư mục nếu chưa tồn tại.
   - Lưu và tải checkpoints mô hình, scaler, kết quả dạng pickle/json/pt.
5. Thiết lập Logging hệ thống chuẩn mực để theo dõi tiến trình.

CÁC HÀM DỰ KIẾN HIỆN THỰC (TODO):
- set_seed(seed: int = 42)
- get_device() -> torch.device
- load_config(config_path: str = "configs/config.yaml") -> dict
- ensure_dirs(dir_list: list[str])
- save_checkpoint(state: dict, filepath: str)
- load_checkpoint(filepath: str, model, optimizer=None)
- setup_logger(name: str, log_file: str = None)
"""

# Lưu ý: Chưa viết mã thực thi, file này chỉ định nghĩa cấu trúc và nhiệm vụ.
