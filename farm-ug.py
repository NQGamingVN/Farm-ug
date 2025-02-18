from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options
from selenium.common.exceptions import NoSuchElementException
import Options
import time

# Thiết lập tùy chọn cho Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Mở cửa sổ trình duyệt ở chế độ tối đa

# Khởi tạo WebDriver
service = Service('path/to/chromedriver')  # Thay đổi đường dẫn đến chromedriver của bạn
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Truy cập vào trang web
    driver.get("https://www.ugphone.com/toc-portal/#/login")

    # Đợi một chút để trang tải xong
    time.sleep(5)

    # Xóa cookie
    driver.delete_all_cookies()

    # Xóa local storage
    driver.execute_script("window.localStorage.clear();")

    print("Đã xóa toàn bộ cookie và local storage.")
    # Vòng lặp để tìm nút với XPath
    while True:
        try:
            # Tìm nút bằng XPath
            button = driver.find_element(By.XPATH, 'nut1')
            button.click()  # Bấm vào nút
            break  # Thoát khỏi vòng lặp nếu nút đã được bấm
        except NoSuchElementException:
            # Nếu không tìm thấy nút, đợi một chút và thử lại
            time.sleep(1)
finally:
    # Đóng trình duyệt
    driver.quit()