from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("D:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

# element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("Flower Girl Bracelet")
# element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(element.text)
# login=driver.find_element(By.LINK_TEXT,"Log in")
# login.click()
#
# elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(elements))
elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(len(elements))
for element in elements:
    print(element.text)