from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("D:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.implicitly_wait(20)
driver.maximize_window()

#absolute/full Xpath:
driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("Jewelry")
driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/ul[1]/li[2]/a").click()

#relative/partial Xpath:
driver.find_element(By.XPATH,"//*[@id='small-searchterms']").send_keys("Jewelry")
driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Electronics']").click()


