from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("D:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")
searchbox=driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Display Status:", searchbox.is_displayed())
print("Display Status:", searchbox.is_enabled())
register = driver.find_element(By.XPATH,"//a[normalize-space()='Register']")
register.click()
male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
male.click()

print(male.is_selected())
print(female.is_selected())
