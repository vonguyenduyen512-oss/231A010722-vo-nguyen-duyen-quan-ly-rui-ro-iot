
"""
tinh_diem_rui_ro.py
--------------------
Script tính điểm rủi ro (Risk = Likelihood x Impact) và phân loại mức độ
theo phương pháp NIST SP 800-30 / ma trận 5x5, dùng để tái tạo lại
Risk Register (Bảng 6.2) và ma trận 5x5 (Bảng 6.3) từ dữ liệu đầu vào thô.

Đầu vào : data/danh_sach_rui_ro_dau_vao.csv  (ID, TaiSan, MoiDeDoa, LoHong, Likelihood, Impact)
Đầu ra  : results/output.csv                 (bổ sung cột DiemRuiRo, MucDo)

Cách chạy:
    python3 src/tinh_diem_rui_ro.py
"""

import csv
import os

INPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "danh_sach_rui_ro_dau_vao.csv")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "results", "output.csv")


def phan_loai_muc_do(diem: int) -> str:
    """Phân loại mức độ rủi ro theo thang điểm L x I (1-25)."""
    if diem >= 20:
        return "Nghiêm trọng"
    if diem >= 15:
        return "Rất cao"
    if diem >= 10:
        return "Cao"
    if diem >= 5:
        return "Trung bình"
    return "Thấp"


def tinh_risk_register(input_path: str = INPUT_PATH) -> list[dict]:
    ket_qua = []
    with open(input_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            l = int(row["Likelihood"])
            i = int(row["Impact"])
            diem = l * i
            ket_qua.append({
                "ID": row["ID"],
                "TaiSan": row["TaiSan"],
                "MoiDeDoa": row["MoiDeDoa"],
                "LoHong": row["LoHong"],
                "Likelihood": l,
                "Impact": i,
                "DiemRuiRo": diem,
                "MucDo": phan_loai_muc_do(diem),
            })
    return ket_qua


def xuat_csv(ket_qua: list[dict], output_path: str = OUTPUT_PATH) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fieldnames = ["ID", "TaiSan", "MoiDeDoa", "LoHong", "Likelihood", "Impact", "DiemRuiRo", "MucDo"]
    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(ket_qua)


def tong_hop_theo_muc_do(ket_qua: list[dict]) -> dict:
    tong_hop = {}
    for r in ket_qua:
        tong_hop[r["MucDo"]] = tong_hop.get(r["MucDo"], 0) + 1
    return tong_hop


if __name__ == "__main__":
    ket_qua = tinh_risk_register()
    xuat_csv(ket_qua)
    print(f"Đã tính {len(ket_qua)} rủi ro, kết quả ghi tại: {OUTPUT_PATH}")
    for muc_do, so_luong in sorted(
        tong_hop_theo_muc_do(ket_qua).items(),
        key=lambda x: ["Thấp", "Trung bình", "Cao", "Rất cao", "Nghiêm trọng"].index(x[0]),
        reverse=True,
    ):
        print(f"  {muc_do}: {so_luong}")
