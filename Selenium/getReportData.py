"""
爬蟲程式-(日期、ID、交易代號)查詢每月報表資料範例
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dateutil import rrule
from datetime import datetime
import time

# Login info
account = "your_account"
password = "your_password"

# 設定 WebDriver 路徑
firefox_driver_path = "C:/Users/geckodriver/geckodriver.exe"
service = Service(firefox_driver_path)
driver = webdriver.Firefox(service=service)

# 設定目標網站 URL
url = "your_login_url"
svcUrl = "your_target_url"
# 打開網頁
driver.get(url)

# 等待頁面元素加載完成
wait = WebDriverWait(driver, 10)

# 登錄網站
username_field = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//input[@placeholder='帳號']")))
password_field = driver.find_element(By.XPATH, "//input[@placeholder='密碼']")

login_button = driver.find_element(By.XPATH, "//button[text()='登入']")
# 輸入資料模擬鍵盤輸入
username_field.send_keys(account)
password_field.send_keys(password)
# 點擊登入按鈕
login_button.click()

# 使用者輸入資訊的變數
start_date = datetime.strptime(input('請輸入起始日期(YYYYMM):'), '%Y%m')
end_date = datetime.strptime(input('請輸入結束日期(YYYYMM):'), '%Y%m')
# 根據每月 計算查詢日期區間
dates = rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date)
id = input('請輸入Id:')

# 輸出console檢查有沒有輸入正確用
print('查詢起日為:' + str(start_date))
print('查詢迄日為:' + str(end_date))
print('查詢的身分證為:' + id)

# 打開目標網頁
driver.get(svcUrl)

# 查詢報表
def searchLogin(txnid):
    wait = WebDriverWait(driver, 10)
    print(txnid)
    for date in dates:
        date = date.strftime('%Y%m')
        # 輸入各項查詢條件欄位
        date_field = wait.until(EC.presence_of_element_located(
            (By.XPATH, "your_input_column_XPATH")))
        date_field.clear()
        date_field.send_keys(date)

        id_field = wait.until(EC.presence_of_element_located(
            (By.XPATH, "your_input_column_XPATH")))
        id_field.send_keys(id)
        txnid_field = wait.until(EC.presence_of_element_located(
            (By.XPATH, "your_input_column_XPATH")))
        txnid_field.clear()
        txnid_field.send_keys(txnid)

        # 點擊查詢報表按鈕
        search_button = driver.find_element(
            By.XPATH, "your_button_XPATH")
        search_button.click()

        time.sleep(10)
        # 匯出報表
        wait = WebDriverWait(driver, 10)
        export_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "your_button_XPATH")))
        export_button.click()
        # 檢查有無匯出報表資料
        try:
            nodata_button = driver.find_element(
                By.XPATH, "your_button_XPATH")
            nodata_button.click()
            print(str(date) + "無資料")
        except:
            print(str(date) + "資料已匯出")

# call方法
searchLogin("your_txn_id")

# 登出
logout_button = driver.find_element(
    By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/button")
logout_button.click()

# 關閉瀏覽器
driver.quit()
