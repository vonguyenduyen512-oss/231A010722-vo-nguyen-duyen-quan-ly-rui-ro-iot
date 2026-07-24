# Quản lý rủi ro bảo mật cho hệ thống IoT quy mô nhỏ

Báo cáo tiểu luận cuối kỳ — Học phần: **Bảo mật IoT**
Trường Đại học Văn Hiến — Khoa Công nghệ Thông tin
Sinh viên: Võ Nguyễn Duyên — MSSV: 231A010722

## Phạm vi nghiên cứu

Đề tài thực hiện quản lý rủi ro bảo mật cho hệ thống IoT quy mô nhỏ (hộ gia đình/phòng thí nghiệm) thông qua:

- Nhận diện tài sản cần bảo vệ (thiết bị IoT, gateway, dữ liệu cảm biến, tài khoản quản trị, firmware, hạ tầng mạng)
- Phân tích mối đe dọa và lỗ hổng bảo mật
- Xây dựng Risk Register và đánh giá rủi ro theo ma trận 5×5 (Risk = Likelihood × Impact)
- Đề xuất biện pháp giảm thiểu ưu tiên cho các rủi ro mức cao
- Xây dựng checklist kiểm tra bảo mật định kỳ

Đề tài đánh giá trên mô hình IoT giả lập, tham khảo các tiêu chuẩn **OWASP IoT Security Project** và **NIST SP 800-30**. Không thực hiện tấn công trên thiết bị thực tế, không thu thập dữ liệu cá nhân thật.

## Nguồn tài liệu tham khảo chính

- OWASP IoT Security Verification Standard (ISVS) — https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS
- OWASP IoT Security Testing Guide (ISTG) — https://github.com/OWASP/owasp-istg
- OWASP Internet of Things Project — https://github.com/OWASP/www-project-internet-of-things
- NIST SP 800-30 Rev.1 — Guide for Conducting Risk Assessments
- NISTIR 8259 — Foundational Cybersecurity Activities for IoT Device Manufacturers

## Cấu trúc repo

```
231A010722-vo-nguyen-duyen-quan-ly-rui-ro-iot/
├── README.md
├── report/
│   ├── 231A010722_VoNguyenDuyen_35_BaoCao.docx
│   └── 231A010722_VoNguyenDuyen_35_BaoCao.pdf
├── slides/
│   └── 231A010722_SlideTrinhBay_DeTai35.pptx      (11 trang)
├── results/
│   └── Risk_Register_va_Ma_tran_Rui_ro.xlsx        (5 sheet: 6.1–6.5)
└── references/
    └── README.md                                    (6 tài liệu tham khảo)
```

## Hướng dẫn sử dụng

1. Đọc báo cáo đầy đủ tại `report/` để nắm bối cảnh, phương pháp và kết quả.
2. Mở `results/Risk_Register_va_Ma_tran_Rui_ro.xlsx`:
   - Sheet `6.1_DanhMucTaiSan`: danh mục 15 tài sản
   - Sheet `6.2_RiskRegister`: 17 rủi ro, tự động phân loại mức độ theo công thức `L × I`
   - Sheet `6.3_MaTran5x5`: ma trận rủi ro 5×5 kèm ID rủi ro tương ứng từng ô
   - Sheet `6.4_KeHoachXuLy`: kế hoạch xử lý 5 rủi ro ưu tiên cao nhất
   - Sheet `6.5_Checklist`: 15 hạng mục kiểm tra định kỳ (tuần/tháng/quý/6 tháng)
3. Xem `slides/231A010722_SlideTrinhBay_DeTai35.pptx` để có bản tóm tắt trình chiếu (11 trang: mở đầu, kiến trúc, phương pháp, kết quả, ma trận rủi ro, kế hoạch xử lý, checklist, kết luận).
4. Đối chiếu `references/README.md` cho danh sách tài liệu tham khảo OWASP/NIST.

## Kết quả chính

Tổng cộng **17 rủi ro bảo mật** trên **15 tài sản** được ghi nhận: 2 mức Nghiêm trọng, 4 mức Rất cao, 4 mức Cao, 7 mức Trung bình. Nhóm rủi ro liên quan đến xác thực/quản lý truy cập và cập nhật firmware chiếm tỷ trọng cao nhất trong các mức nghiêm trọng.

## Cam kết

Toàn bộ thử nghiệm được thực hiện trong môi trường cục bộ, dữ liệu giả lập/được phép. Báo cáo, mã nguồn và minh chứng là kết quả làm việc cá nhân; mọi nội dung kế thừa được trích dẫn rõ ràng. Repo không chứa secret, token, mật khẩu hoặc dữ liệu cá nhân thật.
