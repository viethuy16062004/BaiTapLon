# Dự Án Thu Thập Việc Làm Đà Nẵng
Dự án này sử dụng Python và Selenium để thu thập dữ liệu việc làm từ trang web vieclamdanang.vn, đặc biệt là các tin tuyển dụng về bán hàng tại quận Hải Châu, Đà Nẵng. Dữ liệu thu thập bao gồm: Tiêu đề công việc, Tên công ty, Mức lương, Loại hình công việc, Ngày đăng, và Hạn nộp hồ sơ.

## Yêu Cầu
Python 3.7 trở lên.

Google Chrome (Trình duyệt hỗ trợ cho Selenium).

ChromeDriver (Selenium sẽ tự động tải và cài đặt phiên bản phù hợp).

Kết nối Internet (Để thu thập dữ liệu từ trang web).

## Cài Đặt
### 1.Clone Dự Án Từ GitHub
Trước tiên, bạn cần clone dự án từ GitHub:

git clone https://github.com/viethuy16062004/BaiTapLon
cd BaiTapLon
### 2.Tạo Môi Trường Ảo
Để tránh xung đột giữa các thư viện, bạn nên tạo một môi trường ảo cho dự án:

python -m venv env
Kích hoạt môi trường ảo:

Trên Windows:

env\Scripts\activate.bat

Trên macOS/Linux:

source env/bin/activate
### 3. Cài Đặt Các Thư Viện Cần Thiết
Cài đặt tất cả các thư viện cần thiết cho dự án:

pip install -r requirements.txt
Hoặc nếu không có requirements.txt, bạn có thể cài đặt các thư viện thủ công:

pip install selenium webdriver-manager pandas schedule
### 4. Chạy Dự Án
Chạy file Python chính để bắt đầu thu thập dữ liệu:

python BaiTapLon.py
### 5. Lập Lịch Thu Thập Dữ Liệu
Dự án sẽ tự động thu thập dữ liệu vào lúc 6:00 sáng hàng ngày nhờ vào thư viện schedule. Bạn có thể thay đổi thời gian chạy bằng cách chỉnh sửa đoạn mã sau trong BaiTapLon.py:

schedule.every().day.at("21:24").do(thu_thap_du_lieu)
Lưu ý: Thời gian là theo múi giờ UTC, vì vậy nếu bạn muốn chạy vào lúc 6:00 sáng tại Đà Nẵng (múi giờ UTC+7), bạn cần đặt thời gian là 21:00 UTC.

### 6. Dữ Liệu Được Lưu Ở Đâu?
Dữ liệu thu thập được sẽ được lưu vào file CSV có tên dạng vieclamdanang_YYYY-MM-DD_HH-MM-SS.csv. Ví dụ:

vieclamdanang_2025-05-09_06-00-00.csv
## Mô Tả Mã Nguồn
Selenium: Được sử dụng để tự động hóa trình duyệt và thu thập dữ liệu từ trang web.

WebDriverManager: Giúp tự động tải và quản lý phiên bản phù hợp của ChromeDriver.

Pandas: Được sử dụng để lưu dữ liệu thu thập được vào file CSV.

Schedule: Dùng để lập lịch chạy tự động vào thời gian đã định.

