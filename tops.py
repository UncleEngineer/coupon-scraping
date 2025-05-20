# https://www.tops.co.th/th

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import re
from selenium.webdriver.chrome.options import Options

def extract_discount_and_code_with_conditions(text):
    result = {}

    # ดึงตัวเลขหลังคำว่า "ลด"
    discount_match = re.search(r'ลด\s*฿?(\d+)', text)
    if discount_match:
        result['discount'] = int(discount_match.group(1))
    else:
        result['discount'] = None

    # ดึงโค้ดหลังคำว่า "กรอกโค้ด"
    code_match = re.search(r'กรอกโค้ด:\s*([A-Z0-9]+)', text)
    if code_match:
        result['code'] = code_match.group(1)
    else:
        result['code'] = None

    # ดึงจำนวนเงินที่ต้องช็อปครบหลังคำว่า "เมื่อช็อปครบ"
    shop_condition_match = re.search(r'เมื่อช็อป[^:]+ครบ\s*฿?([\d,]+).*?ใบเสร็จ', text)
    if shop_condition_match:
        result['shop_condition'] = shop_condition_match.group(0).strip().replace('\n','').split('ใบเสร็จ')[0] + 'ใบเสร็จ'  # เก็บข้อความเต็มๆ
    else:
        result['shop_condition'] = None

    # ดึงเงื่อนไขหลังคำว่า "เฉพาะวันสั่งซื้อ" และก่อน "-สิทธิพิเศษ"
    condition_match = re.search(r'เฉพาะวันสั่งซื้อ(.*?)\s*- สิทธิพิเศษ', text, re.DOTALL)
    if condition_match:
        # ลบอักขระพิเศษออก
        result['condition'] = condition_match.group(1).strip()[2:]
    else:
        result['condition'] = None

    return result


chrome_options = Options()
chrome_options.add_argument('--headless')  # เปิดโหมด headless
chrome_options.add_argument('--disable-gpu')  # ปิด GPU acceleration (ช่วยลดปัญหาบางอย่าง)
chrome_options.add_argument('--no-sandbox')  # เพิ่มความเสถียรในบางระบบ

# เริ่ม Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome()
driver.get("https://www.tops.co.th/th")

time.sleep(5)

html = driver.page_source
time.sleep(2)

soup = BeautifulSoup(html,'html.parser')

coupon = soup.find_all('div',{'class':'coupon-slider__slide-item bgTypeColorDropdown coupon-slider__slide--black-img'})
for cp in coupon:
    # print()
    result = extract_discount_and_code_with_conditions(cp.text)
    print(result)
    print('----------')

# with open('output_tops.html','w',encoding='utf-8') as file:
#     file.write(html)

driver.quit()
print('headless success')