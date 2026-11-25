# ==============================================================================
# File: src/trainer.py
# Nhiệm vụ: Training Loop, Validation, Optimizer, Early Stopping, Checkpoint
# ==============================================================================
"""
MÔ TẢ CHI TIẾT NHIỆM VỤ:
1. Xây dựng vòng lặp huấn luyện chuẩn cho Deep Learning (PyTorch):
   - Epoch training loop với Batch gradient descent.
   - Validation loop sau mỗi epoch để theo dõi loss và metrics.
2. Quản lý Optimizer và Learning Rate Scheduler:
   - Hỗ trợ Adam, AdamW, SGD, RMSprop.
   - Hỗ trợ ReduceLROnPlateau, CosineAnnealingLR.
3. Cơ chế Early Stopping:
   - Dừng huấn luyện khi validation loss không cải thiện sau số epoch chỉ định (patience).
   - Ngăn chặn triệt để overfitting trên tập train.
4. Quản lý Checkpoints:
   - Lưu trọng số tốt nhất của mô hình (`best_model.pt`) vào `artifacts/models/`.
   - Lưu lịch sử huấn luyện (train_loss, val_loss, train_acc, val_acc) phục vụ vẽ Learning Curves.

CÁC LỚP VÀ HÀM DỰ KIẾN HIỆN THỰC (TODO):
- class EarlyStopping:
  + __init__(self, patience: int = 10, delta: float = 0.0, checkpoint_path: str = "artifacts/models/best_model.pt")
  + __call__(self, val_loss: float, model: nn.Module)
- class ModelTrainer:
  + __init__(self, model, optimizer, criterion, device, scheduler=None)
  + train_epoch(self, dataloader) -> Tuple[float, float]
  + validate(self, dataloader) -> Tuple[float, float]
  + fit(self, train_loader, val_loader, epochs: int, early_stopping: EarlyStopping) -> dict
"""

# Lưu ý: Chưa viết mã thực thi, file này chỉ định nghĩa cấu trúc và nhiệm vụ.
