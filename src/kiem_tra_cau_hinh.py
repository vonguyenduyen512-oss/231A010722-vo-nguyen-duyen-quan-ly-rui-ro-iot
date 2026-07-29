"""
kiem_tra_cau_hinh.py
---------------------
Script quét tự động cấu hình MQTT broker (mosquitto.conf) và ACL (aclfile)
nhằm phát hiện các lỗ hổng phổ biến theo OWASP IoT Top 10 / ISVS
(Communication security). Đây là bước "automated configuration audit"
bổ sung cho phần đánh giá thủ công tại mục 5.2 của báo cáo — không thực
hiện bất kỳ thao tác kết nối, quét cổng hay khai thác nào trên thiết bị
hoặc mạng thật, chỉ đọc và phân tích tĩnh (static analysis) các file
cấu hình mô phỏng có sẵn trong repo (configs/).

Đầu vào : configs/mosquitto.conf, configs/aclfile
Đầu ra  : results/output_audit_config.csv (danh sách phát hiện + mức độ)

Cách chạy:
    python3 src/kiem_tra_cau_hinh.py
"""

import csv
import os
import re

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
MOSQUITTO_PATH = os.path.join(BASE_DIR, "configs", "mosquitto.conf")
ACL_PATH = os.path.join(BASE_DIR, "configs", "aclfile")
OUTPUT_PATH = os.path.join(BASE_DIR, "results", "output_audit_config.csv")


def doc_file(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        return f.readlines()


def quet_mosquitto(dong: list[str]) -> list[dict]:
    """Quét mosquitto.conf, bỏ qua dòng comment, tìm các chỉ thị rủi ro."""
    phat_hien = []
    noi_dung = [d for d in dong if not d.strip().startswith("#") and d.strip()]
    van_ban = "".join(noi_dung)

    if re.search(r"allow_anonymous\s+true", van_ban):
        phat_hien.append({
            "HangMuc": "allow_anonymous",
            "PhatHien": "Broker cho phép kết nối ẩn danh (allow_anonymous true)",
            "MucDo": "Nghiêm trọng",
            "KhuyenNghi": "Đặt allow_anonymous false và bắt buộc xác thực user/password hoặc chứng chỉ",
        })

    if not re.search(r"listener\s+8883", van_ban):
        phat_hien.append({
            "HangMuc": "TLS/mã hóa kênh truyền",
            "PhatHien": "Không tìm thấy listener 8883 (cổng TLS) — dữ liệu truyền không mã hóa",
            "MucDo": "Cao",
            "KhuyenNghi": "Bật listener 8883 kèm certfile/keyfile (TLS) cho toàn bộ kết nối MQTT",
        })

    if not re.search(r"password_file", van_ban):
        phat_hien.append({
            "HangMuc": "Xác thực user/password",
            "PhatHien": "Không cấu hình password_file cho broker",
            "MucDo": "Cao",
            "KhuyenNghi": "Thiết lập password_file và acl_file để kiểm soát truy cập theo user",
        })

    return phat_hien


def quet_acl(dong: list[str]) -> list[dict]:
    """Quét aclfile, kiểm tra phạm vi quyền của từng user."""
    phat_hien = []
    noi_dung = [d for d in dong if not d.strip().startswith("#") and d.strip()]
    van_ban = "".join(noi_dung)

    if re.search(r"topic\s+readwrite\s+home/#", van_ban):
        phat_hien.append({
            "HangMuc": "Phạm vi quyền ACL",
            "PhatHien": "Có user được cấp quyền readwrite trên toàn bộ topic (home/#)",
            "MucDo": "Trung bình",
            "KhuyenNghi": "Giới hạn quyền theo nguyên tắc least privilege — chỉ cấp topic cần thiết cho từng vai trò",
        })

    return phat_hien


def xuat_csv(ket_qua: list[dict], output_path: str = OUTPUT_PATH) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fieldnames = ["HangMuc", "PhatHien", "MucDo", "KhuyenNghi"]
    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(ket_qua)


if __name__ == "__main__":
    ket_qua = quet_mosquitto(doc_file(MOSQUITTO_PATH)) + quet_acl(doc_file(ACL_PATH))
    xuat_csv(ket_qua)
    print(f"Đã quét cấu hình, phát hiện {len(ket_qua)} vấn đề. Kết quả ghi tại: {OUTPUT_PATH}")
    for kq in ket_qua:
        print(f"  [{kq['MucDo']}] {kq['HangMuc']}: {kq['PhatHien']}")
