from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import schedule
import datetime
import os

# Hàm chính để thu thập dữ liệu
def crawl_data():
    print(f" Bắt đầu chạy lúc {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 15)

    data = []
    page = 1

    # 5. Lấy tất cả dữ liệu của các trang.
    while True:
        url = f"https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/3/da-nang/trang--{page}.html"
        print(f" Đang thu thập trang {page}: {url}")
        driver.get(url)
        time.sleep(3)

        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".content-item.item")))
        except:
            print(" Không tìm thấy dữ liệu hoặc hết trang.")
            break

        listings = driver.find_elements(By.CSS_SELECTOR, ".content-item.item")
        if not listings:
            break

    # 4. Lấy tất cả dữ liệu(Tiêu đề, Mô tả, Địa chỉ, Diện tích, Giá) hiển thị ở bài viết.
        for listing in listings:
            try:
                title = listing.find_element(By.CSS_SELECTOR, ".ct_title").text.strip()
                description = listing.find_element(By.CSS_SELECTOR, ".ct_brief").text.strip()
                try:
                    area = listing.find_element(By.CSS_SELECTOR, ".road-width").text.strip()
                except:
                    area = "Không có thông tin"
                try:
                    price = listing.find_element(By.CSS_SELECTOR, ".ct_price").text.strip()
                except:
                    price = "Không có giá"
                try:
                    address = listing.find_element(By.CSS_SELECTOR, ".ct_dis").text.strip()
                except:
                    address = "Không có địa chỉ"

                data.append([title, description, area, price, address])
            except Exception as e:
                print(f"Lỗi lấy tin: {e}")
                continue

        page += 1

    driver.quit()

    # 6. Lưu dữ liệu đã lấy được vào file excel hoặc csv.
    df = pd.DataFrame(data, columns=["Tiêu đề", "Mô tả", "Diện tích", "Giá", "Địa chỉ"])
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"alonhadat_danang_{today}.xlsx"
    df.to_excel(filename, index=False)
    print(f" Đã lưu dữ liệu vào: {filename}")

    # 7. Set lịch chạy vào lúc 6h sáng hằng ngày.
schedule.every().day.at("06:00").do(crawl_data)

print(" Đang chờ đến 6h sáng mỗi ngày để chạy crawler")
while True:
    schedule.run_pending()
    time.sleep(60)
