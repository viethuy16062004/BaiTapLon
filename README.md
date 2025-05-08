#  Alonhadat Da Nang Crawler

Một script tự động thu thập dữ liệu bất động sản tại Đà Nẵng từ website [alonhadat.com.vn](https://alonhadat.com.vn), bao gồm: **Tiêu đề, Mô tả, Địa chỉ, Diện tích, Giá** từ tất cả các trang.  
Dữ liệu sẽ được lưu vào file Excel (.xlsx) và tự động chạy **lúc 6h sáng mỗi ngày**.

---

##  Tính năng

- Tự động thu thập dữ liệu bất động sản từ nhiều trang.
- Trích xuất đầy đủ thông tin: Tiêu đề, Mô tả, Địa chỉ, Diện tích, Giá.
- Lưu dữ liệu vào file Excel theo ngày.
- Tự động chạy theo lịch định sẵn mỗi ngày lúc 06:00 sáng.
- Có thể mở rộng ra các khu vực khác hoặc website khác.

---

##  Yêu cầu hệ thống

- Python 3.8 trở lên
- Google Chrome đã cài đặt
- Trình quản lý gói `pip`

---

##  Cài đặt

### Bước 1: Clone project

git clone https://github.com/ten-cua-ban/alonhadat-crawler.git
cd alonhadat-crawler
### Bước 2: Tạo môi trường ảo (khuyên dùng)

python -m venv venv
#### Windows:
venv\Scripts\activate
#### macOS/Linux:
source venv/bin/activate
### Bước 3: Cài đặt thư viện

pip install -r requirements.txt

Nếu chưa có file requirements.txt, bạn có thể tạo bằng lệnh:

pip freeze > requirements.txt
## Cách sử dụng
Chạy thủ công
Chạy script một lần để lấy dữ liệu ngay:
python crawler.py
Chạy tự động mỗi ngày
Script sử dụng thư viện schedule để tự động chạy lúc 06:00 sáng mỗi ngày.

Chỉ cần chạy:

python crawler.py
Và để máy chạy liên tục hoặc cấu hình với Task Scheduler (Windows) hoặc crontab (Linux/macOS) để chạy nền.

 Dữ liệu đầu ra
File Excel sẽ được lưu theo ngày, ví dụ:
alonhadat_danang_2025-05-08.xlsx
Bạn có thể sửa code để lưu thành .csv nếu cần:
df.to_csv("alonhadat_danang_2025-05-08.csv", index=False)
