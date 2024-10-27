import time
import json
from seleniumwire import webdriver  # برای رهگیری درخواست‌ها
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime  # برای ثبت زمان
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# تنظیمات کروم برای اندروید
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-proxy-server')  # غیرفعال کردن استفاده از پروکسی


#اینجا مررورگر نصب میکنه و دانلود میکنه
service = Service(ChromeDriverManager().install())

#اینجا تنظیمات که برای مرورگر تنظیم کردیم و فایل مروگر وارد میکنه دارایور میسازه اماده میکنه
driver = webdriver.Chrome(service=service, options=chrome_options)


#این تابع برای کلیک
def click_element(xpath):
    element = driver.find_element(By.XPATH, xpath)
    element.click()

# تابعی برای تایپ کردن بر اساس XPath
def type_in_element(xpath, text):
    element = driver.find_element(By.XPATH, xpath)
    element.send_keys(text)


#اینم سایت برا اول باز میکنه
driver.get('https://m.snappfood.org/')

time.sleep(5)


#کلیک روی انتخب نقشه
click_element('/html/body/div[2]/div[1]/div/div/div[2]/button')

time.sleep(2)

#کلیک روی دکمه ورود در منو پایین
click_element('/html/body/div[1]/div[3]/div')
time.sleep(0.5)


#کلیک روی دکمه عضویت
click_element('/html/body/div[1]/div[4]/div/div/div[3]/button')
time.sleep(0.5)


#کلیک روی اینپوت شماره همراه
click_element('/html/body/div[1]/div[2]/section/div[1]/div[3]/div[1]/input')
time.sleep(0.5)

#تایپ شماره همراه روی اینپوت شماره همراه
type_in_element('/html/body/div[1]/div[2]/section/div[1]/div[3]/div[1]/input','09000000')

time.sleep(10)









