from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://uncle-book.com/admin/login")

elem = driver.find_element(By.NAME, "username")
elem.clear()
elem.send_keys("manager")
elem = driver.find_element(By.NAME, "password")
elem.clear()
elem.send_keys("pass456")
elem.send_keys(Keys.RETURN)
time.sleep(3)

# driver.get("https://uncle-book.com/admin/contacts")
# time.sleep(3)

html = driver.page_source


soup = BeautifulSoup(html,'html.parser')
table = soup.find('table',{'class':'table table-bordered table-striped'})

tablerow = table.find_all('tr')

for row in tablerow[1:]:
    # tablerow[1:] คือ เอาแถวที่ 1 ขึ้นไป
    # print(row)
    td = row.find_all('td')
    print('Name: ',td[1].text)
    print('Detail: ',td[2].text)
    print('------------')

# 'table table-bordered table-striped'

time.sleep(30)
driver.quit()