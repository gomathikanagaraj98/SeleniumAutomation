from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("D:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

# driver.get("http://the-internet.herokuapp.com/javascript_alerts")
driver.get("http://admin:admin@the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()