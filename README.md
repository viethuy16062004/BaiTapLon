# Hướng Dẫn Cài Đặt Dự Án Thu Thập Việc Làm Đà Nẵng

Dự án sử dụng Python và Selenium để thu thập dữ liệu từ trang [vieclamdanang.vn].

## Yêu cầu

- Python 3.7 trở lên  
- Trình duyệt Google Chrome  
- Kết nối Internet  
---

## Cài đặt

### 1. Clone dự án từ GitHub

git clone https://github.com/viethuy16062004/BaiTapLon
cd BaiTapLon.py

### 2.Tạo môi trường ảo 
python -m venv env
env\Scripts\activate.bat     # Trên Windows
### 3.Cài đặt thư viện cần thiết
Nếu có file requirements.txt:
pip install -r requirements.txt
Hoặc cài trực tiếp:

pip install selenium webdriver-manager pandas schedule
### 4.Kiểm tra chạy thử
Chạy file Python:
python BaiTapLon.py

