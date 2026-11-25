# ==============================================================================
# Final-ML-Stock-Prediction Source Package
# ==============================================================================
"""
Package src: Chứa toàn bộ mã nguồn xử lý dữ liệu, trích xuất đặc trưng,
định nghĩa mô hình, huấn luyện, đánh giá và tiện ích cho bài toán dự đoán giá/xu hướng chứng khoán.
"""

import os
import shutil
import tempfile
import certifi


def _setup_ssl_certs():
    """
    Khắc phục lỗi curl (77) / SSLError trên Windows khi đường dẫn thư mục chứa
    ký tự tiếng Việt có dấu (ví dụ: 'Chính thức', 'Năm 3').
    Copy file cacert.pem sang thư mục tạm có đường dẫn thuần ASCII và gán biến môi trường.
    """
    try:
        ca_path = certifi.where()
        need_fix = False
        try:
            ca_path.encode('ascii')
        except UnicodeEncodeError:
            need_fix = True

        if need_fix or " " in ca_path:
            temp_dir = tempfile.gettempdir()
            try:
                temp_dir.encode('ascii')
            except UnicodeEncodeError:
                temp_dir = os.environ.get("SystemRoot", "C:\\Windows") + "\\Temp"

            safe_ca_path = os.path.join(temp_dir, "cacert.pem")
            if not os.path.exists(safe_ca_path) or os.path.getsize(safe_ca_path) != os.path.getsize(ca_path):
                shutil.copyfile(ca_path, safe_ca_path)
            os.environ["CURL_CA_BUNDLE"] = safe_ca_path
            os.environ["SSL_CERT_FILE"] = safe_ca_path
    except Exception:
        pass


_setup_ssl_certs()


