from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("D:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://www.snapdeal.com")
driver.get("https://www.amazon.com")

driver.back()
driver.forward()
driver.refresh()

driver.quit()