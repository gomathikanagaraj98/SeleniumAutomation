from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("D:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)


driver.get("https://automationpractice.com/index.php")
driver.implicitly_wait(20)
driver.maximize_window()
#sliders=driver.find_elements(By.CLASS_NAME,"homeslider")
# print(len(sliders))
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))