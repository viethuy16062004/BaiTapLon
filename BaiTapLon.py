from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import datetime
import schedule

def thu_thap_du_lieu():
    print(f"Bắt đầu lúc: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    dich_vu = Service(ChromeDriverManager().install())
    trinh_duyet = webdriver.Chrome(service=dich_vu)
    cho_cho = WebDriverWait(trinh_duyet, 15)
    du_lieu = []
    trang = 1

    # (5) Lấy tất cả dữ liệu của các trang.
    while True:
        url = f"https://vieclamdanang.vn/tim-kiem/viec-lam-ban-hang-tai-hai-chau?page={trang}&cat=13&dis=1&order=1"
        print(f"Đang thu thập trang {trang}: {url}")
        trinh_duyet.get(url)
        time.sleep(3)
        try:
            cho_cho.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".box-job-horizontal")))
        except:
            print("Không còn dữ liệu. Dừng lại.")
            break
        danh_sach = trinh_duyet.find_elements(By.CSS_SELECTOR, ".box-job-horizontal")
        if not danh_sach:
            break

        for bai_viet in danh_sach:
            try:
                # (4) Lấy tất cả dữ liệu: Tiêu đề, Mô tả, Tên Công ty, Mức lương, Địa điểm hiển thị ở bài viết
                tieu_de = bai_viet.find_element(By.CSS_SELECTOR, ".job-name a").text.strip()
                cong_ty = bai_viet.find_element(By.CSS_SELECTOR, ".job-company").text.strip()
                try:
                    muc_luong = bai_viet.find_element(By.CSS_SELECTOR, "._salary span").text.strip()
                except:
                    muc_luong = ""
                try:
                    loai_hinh = bai_viet.find_element(By.CSS_SELECTOR, ".job-type").text.strip()
                except:
                    loai_hinh = ""
                try:
                    ngay_dang = bai_viet.find_element(By.CSS_SELECTOR, "._date span").text.strip()
                except:
                    ngay_dang = ""
                try:
                    han_nop = bai_viet.find_element(By.CSS_SELECTOR, "._exp span[style='color:#dd263c']").text.strip()
                except:
                    han_nop = ""
                du_lieu.append([tieu_de, cong_ty, muc_luong, loai_hinh, ngay_dang, han_nop])
            except Exception as loi:
                print(f"Lỗi khi lấy dữ liệu tin tuyển dụng: {loi}")
                continue
        trang += 1
    trinh_duyet.quit()

    # (6) Lưu dữ liệu đã lấy được vào file excel hoặc csv.
    df = pd.DataFrame(du_lieu, columns=["Tiêu đề", "Công ty", "Mức lương", "Loại hình", "Ngày đăng", "Hạn nộp hồ sơ"])
    ngay_gio = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    ten_tap_tin = f"vieclamdanang_{ngay_gio}.csv"
    df.to_csv(ten_tap_tin, index=False, encoding='utf-8-sig')
    print(f"Đã lưu dữ liệu vào file: {ten_tap_tin}")

# (7) Set lịch chạy vào lúc 6h sáng hằng ngày.
schedule.every().day.at("21:24").do(thu_thap_du_lieu)
print("Đang chờ đến thời gian được đặt để chạy")
while True:
    schedule.run_pending()
    time.sleep(60)
