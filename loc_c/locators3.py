from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("D:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.implicitly_wait(20)
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("bbb")
driver.find_element(By.CSS_SELECTOR,"#email").send_keys("bbb")

driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("aaa@gmail.com")
driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("aaa@gmail.com")

driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email").send_keys("ccc")
driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email").send_keys("ccc")

driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass").send_keys("xxx")


