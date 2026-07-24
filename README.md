# Quản lý rủi ro bảo mật cho hệ thống IoT quy mô nhỏ

Báo cáo tiểu luận cuối kỳ – Học phần: **Bảo mật IoT**  
Trường Đại học Văn Hiến – Khoa Công nghệ Thông tin

**Sinh viên:** Võ Nguyễn Duyên  
**MSSV:** 231A010722

---

## Phạm vi nghiên cứu

Đề tài xây dựng mô hình quản lý rủi ro bảo mật cho hệ thống IoT quy mô nhỏ (hộ gia đình/phòng thí nghiệm) thông qua:

- Nhận diện các tài sản cần bảo vệ.
- Phân tích mối đe dọa và lỗ hổng bảo mật.
- Xây dựng Risk Register.
- Đánh giá rủi ro theo ma trận 5×5 (Risk = Likelihood × Impact).
- Đề xuất biện pháp giảm thiểu theo mức độ ưu tiên.
- Xây dựng checklist kiểm tra bảo mật định kỳ.

Đề tài được thực hiện trên mô hình IoT giả lập, tham khảo các tiêu chuẩn **OWASP IoT Security Project**, **OWASP ISVS** và **NIST SP 800-30**. Mọi thử nghiệm đều được thực hiện trong môi trường học tập, không tấn công hệ thống thực tế và không sử dụng dữ liệu cá nhân.

---

## Nguồn tài liệu tham khảo chính

- OWASP IoT Security Verification Standard (ISVS)
- OWASP IoT Security Testing Guide (ISTG)
- OWASP Internet of Things Project
- NIST SP 800-30 Rev.1 – Guide for Conducting Risk Assessments
- NISTIR 8259 – Foundational Cybersecurity Activities for IoT Device Manufacturers
- Node-RED Community

---


## Cấu trúc repository
```text

231A010722-vo-nguyen-duyen-quan-ly-rui-ro-iot/
├── README.md
├── report/
│ ├── 231A010722-VONGUYENDUYEN-BAOCAOTIEULUAN-DE TAI 35.docx
│ └── 231A010722-VONGUYENDUYEN-BAOCAOTIEULUAN-DE TAI 35.pdf
├── slides/
├──  231A010722- SLIEDE TRINH BAY DE TAI 35.pptx
│ └──  231A010722- SLIEDE TRINH BAY DE TAI 35.pptx.pdf

├── results/
│ └── Risk_Register_va_Ma_tran_Rui_ro.xlsx
└── references/
└── link_nguon.md
```
---

## Hướng dẫn sử dụng

1. Đọc báo cáo trong thư mục `report/`.
2. Mở tệp `results/Risk_Register_va_Ma_tran_Rui_ro.xlsx`:
   - **Sheet `6.1_DanhMucTaiSan`:** Danh mục tài sản.
   - **Sheet `RiskRegister_6.2-6.3`:** Risk Register (mối đe dọa, lỗ hổng, điểm rủi ro, biện pháp, rủi ro còn lại).
   - **Sheet `MaTran5x5_TrucQuan`:** Ma trận rủi ro 5×5 dạng trực quan.
   - **Sheet `6.4_Checklist`:** Checklist kiểm tra bảo mật định kỳ.
3. Xem file `slides/231A010722_SlideTrinhBay_DeTai35.pptx` để trình bày nội dung tóm tắt.
4. Tham khảo danh sách tài liệu trong `references/link_nguon.md`.

---

## Kết quả chính

Đề tài xây dựng:

- Danh mục **6 tài sản** cần bảo vệ.
- **6 rủi ro bảo mật** được đánh giá bằng Risk Register.
- Ma trận đánh giá rủi ro **5×5**.
- Kế hoạch giảm thiểu cho toàn bộ các rủi ro.
- Checklist kiểm tra bảo mật định kỳ.

Kết quả đánh giá ghi nhận:

- **2 rủi ro mức Nghiêm trọng**
- **4 rủi ro mức Rất cao**

Các rủi ro liên quan đến **mật khẩu yếu**, **firmware chưa cập nhật**, **truy cập từ xa**, và **xác thực tài khoản** là những vấn đề cần ưu tiên xử lý.

---

## Cam kết

- Toàn bộ nội dung được thực hiện trong môi trường học tập và nghiên cứu.
- Không sử dụng dữ liệu cá nhân thật.
- Không chứa secret, token, mật khẩu hoặc thông tin nhạy cảm.
- Mọi tài liệu tham khảo đều được trích dẫn đầy đủ theo báo cáo.
