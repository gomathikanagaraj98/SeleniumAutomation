from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj=Service("D:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.quit()