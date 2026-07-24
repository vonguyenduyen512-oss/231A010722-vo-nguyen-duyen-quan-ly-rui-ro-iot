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
├── report/       # Báo cáo đầy đủ (.docx, .pdf) + sơ đồ Hình 2.1/2.2/3.1/3.2
├── slides/       # Bản trình chiếu (.pptx)
├── results/      # Risk Register, ma trận 5x5, kế hoạch xử lý, checklist (Bảng 6.1-6.5)
└── references/   # Tài liệu tham khảo OWASP, NIST
```

## Hướng dẫn sử dụng

1. Đọc báo cáo đầy đủ tại `report/` để nắm bối cảnh, phương pháp và kết quả.
2. Mở file Risk Register trong `results/` để tra cứu mức độ rủi ro theo từng tài sản.
3. Đối chiếu với ma trận 5×5 để xác định thứ tự ưu tiên xử lý.
4. Sử dụng checklist (Bảng 6.5) theo tần suất tuần/tháng/quý để duy trì kiểm tra bảo mật định kỳ.

## Kết quả chính

Tổng cộng **17 rủi ro bảo mật** trên **15 tài sản** được ghi nhận: 2 mức Nghiêm trọng, 4 mức Rất cao, 4 mức Cao, 7 mức Trung bình. Nhóm rủi ro liên quan đến xác thực/quản lý truy cập và cập nhật firmware chiếm tỷ trọng cao nhất trong các mức nghiêm trọng.

## Cam kết

Toàn bộ thử nghiệm được thực hiện trong môi trường cục bộ, dữ liệu giả lập/được phép. Báo cáo, mã nguồn và minh chứng là kết quả làm việc cá nhân; mọi nội dung kế thừa được trích dẫn rõ ràng. Repo không chứa secret, token, mật khẩu hoặc dữ liệu cá nhân thật.
