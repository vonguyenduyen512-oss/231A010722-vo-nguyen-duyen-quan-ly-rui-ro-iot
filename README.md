# Quản lý rủi ro bảo mật cho hệ thống IoT quy mô nhỏ

Báo cáo tiểu luận cuối kỳ – Học phần: **Bảo mật IoT (INT4410)**
Trường Đại học Văn Hiến – Khoa Công nghệ Thông tin

**Sinh viên:** Võ Nguyễn Duyên
**MSSV:** 231A010722
**Đề tài:** 35 — Quản lý rủi ro bảo mật cho hệ thống IoT quy mô nhỏ (Hướng G)

---

## Phạm vi nghiên cứu

Đề tài xây dựng mô hình quản lý rủi ro bảo mật cho hệ thống IoT quy mô nhỏ (hộ gia đình/phòng thí nghiệm) thông qua:

- Nhận diện các tài sản cần bảo vệ.
- Phân tích mối đe dọa và lỗ hổng bảo mật.
- Xây dựng Risk Register.
- Đánh giá rủi ro theo ma trận 5×5 (Điểm = Khả năng × Tác động).
- Đề xuất biện pháp giảm thiểu theo mức độ ưu tiên.
- Xây dựng checklist kiểm tra bảo mật định kỳ.

Đề tài được thực hiện trên mô hình IoT giả lập, tham khảo các tiêu chuẩn **OWASP IoT Security Project**, **OWASP ISVS/ISTG** và **NIST SP 800-30**. Mọi thử nghiệm đều được thực hiện trong môi trường học tập, không tấn công hệ thống thực tế và không sử dụng dữ liệu cá nhân.

---

## Nguồn tài liệu tham khảo chính

1. OWASP Foundation – OWASP IoT Security Verification Standard (ISVS)
2. OWASP Foundation – OWASP IoT Security Testing Guide (ISTG)
3. OWASP Foundation – OWASP Internet of Things Project
4. Russell, B.; Van Duren, D. – *Practical IoT Security*, Packt Publishing, 2016
5. NIST – SP 800-30 Rev.1, Guide for Conducting Risk Assessments
6. NIST – NISTIR 8259, Foundational Cybersecurity Activities for IoT Device Manufacturers
7. IoT Acceleration Consortium; MIC; METI – IoT Security Guidelines Ver. 1.0
8. Node-RED Community – Node-RED

Danh sách đầy đủ kèm URL và ngày truy cập: xem `references/link_nguon.md` và mục "TÀI LIỆU THAM KHẢO" trong báo cáo.

---

## Cấu trúc repository

```text
231A010722-vo-nguyen-duyen-quan-ly-rui-ro-iot/
├── README.md
├── report/
│   ├── 231A010722_VoNguyenDuyen_DeTai35_TieuLuan_CuoiKy.docx
│   └── 231A010722_VoNguyenDuyen_DeTai35_TieuLuan_CuoiKy.pdf
├── slides/
│   
├── results/
│   ├── Risk_Register_va_Ma_tran_Rui_ro.xlsx
│   ├── output.csv                  (kết quả script tinh_diem_rui_ro.py)
│   ├── screenshots/                (Hình 4.1–4.3 dùng trong báo cáo)
│   │   ├── hinh4.1_danh_muc_tai_san.png
│   │   ├── hinh4.2_risk_register.png
│   │   └── hinh4.3_ma_tran_5x5.png
│   └── logs/
│       └── log_chay_script.txt     (nhật ký chạy script — xem Bảng A.1, Phụ lục A)
├── src/
│   └── tinh_diem_rui_ro.py         (script tính điểm rủi ro L×I và phân loại mức độ)
├── data/
│   ├── danh_sach_rui_ro_dau_vao.csv
│   └── payload_mau.json            (payload mô phỏng, không phải dữ liệu thật)
├── configs/
│   ├── manifest.json               (danh mục tài sản kỹ thuật đầy đủ)
│   ├── flow.json                   (luồng dữ liệu, khớp Hình 2.1/3.1)
│   ├── mosquitto.conf              (cấu hình MQTT broker khảo sát — minh chứng lỗ hổng)
│   └── aclfile                     (ACL đề xuất khắc phục — mục 5.4)
└── references/
    └── link_nguon.md
```

---

## Hướng dẫn sử dụng

1. Đọc báo cáo đầy đủ trong `report/231A010722_VoNguyenDuyen_DeTai35_TieuLuan_CuoiKy.docx` (hoặc bản `.pdf` đi kèm).
2. Mở `results/Risk_Register_va_Ma_tran_Rui_ro.xlsx`:
   - **Sheet `5.1_DanhMucTaiSan`:** Danh mục tài sản (khớp Bảng 5.1 báo cáo).
   - **Sheet `RiskRegister_5.2-5.3`:** Mối đe dọa, lỗ hổng, điểm rủi ro, biện pháp, rủi ro còn lại (khớp Bảng 5.2–5.3).
   - **Sheet `MaTran5x5_TrucQuan`:** Ma trận rủi ro 5×5 dạng trực quan (khớp Hình 4.3).
   - **Sheet `5.4_Checklist`:** Checklist kiểm tra bảo mật định kỳ (khớp Bảng 5.4).
3. Chạy lại script tính điểm rủi ro nếu cần tái tạo kết quả:
   ```bash
   python3 src/tinh_diem_rui_ro.py
   ```
   Đầu vào: `data/danh_sach_rui_ro_dau_vao.csv` — Đầu ra: `results/output.csv`. Nhật ký lần chạy gần nhất: `results/logs/log_chay_script.txt`.
4. Xem `slides/231A010722_VoNguyenDuyen_DeTai35_SlideTrinhBay.pptx` (hoặc bản `.pdf` đi kèm) để xem nội dung tóm tắt (12 trang: bối cảnh → phạm vi → kiến trúc → phương pháp → kết quả → Risk Register → ma trận 5×5 → kế hoạch xử lý → vận hành → kết luận).
5. Tham khảo danh sách tài liệu đầy đủ trong `references/link_nguon.md`.

---

## Kết quả chính

Đề tài xây dựng:

- Danh mục **6 tài sản quan trọng nhất** (Bảng 5.1) được chọn lọc từ danh mục kỹ thuật đầy đủ 15 tài sản (`configs/manifest.json`).
- **6 rủi ro bảo mật** (R-01 → R-06) được đánh giá bằng Risk Register (Bảng 5.2).
- Ma trận đánh giá rủi ro **5×5** (Bảng 5.3, Hình 4.3).
- Kế hoạch giảm thiểu cho toàn bộ 6 rủi ro theo thứ tự ưu tiên (mục 5.4).
- Checklist kiểm tra bảo mật định kỳ gồm 6 hạng mục (Bảng 5.4).

Kết quả đánh giá ghi nhận (script `src/tinh_diem_rui_ro.py`, xem `results/output.csv`):

- **2 rủi ro mức Nghiêm trọng** (R-01, R-02)
- **4 rủi ro mức Rất cao** (R-03, R-04, R-05, R-06)

Các rủi ro liên quan đến **mật khẩu yếu**, **firmware chưa cập nhật**, **truy cập từ xa không kiểm soát**, và **thiếu xác thực đa yếu tố** là những vấn đề cần ưu tiên xử lý. Cấu hình `configs/mosquitto.conf` và `configs/aclfile` minh họa thêm lỗ hổng và biện pháp khắc phục ở tầng giao thức MQTT (bổ trợ cho mục 5.4, ngoài 6 rủi ro chính).

---

## Cam kết

- Toàn bộ nội dung được thực hiện trong môi trường học tập và nghiên cứu (mô phỏng).
- Không sử dụng dữ liệu cá nhân thật; `payload_mau.json` chỉ là dữ liệu minh họa.
- Không chứa secret, token, mật khẩu hoặc thông tin nhạy cảm.
- Mọi tài liệu tham khảo đều được trích dẫn đầy đủ theo báo cáo và `references/link_nguon.md`.
