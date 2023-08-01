import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("D:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(20)
driver.close()
#driver.quit()