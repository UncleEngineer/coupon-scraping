from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.python.org")

elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")

time.sleep(10)

elem.send_keys(Keys.RETURN)

time.sleep(60)
driver.quit()