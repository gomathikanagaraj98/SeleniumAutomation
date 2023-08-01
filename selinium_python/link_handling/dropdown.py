from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("D:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

# dropdown_ele=driver.find_element(By.XPATH,"//select[@id='input-country']")
dropdown=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

# dropdown.select_by_visible_text("Algeria")
# dropdown.select_by_index(13)
# dropdown.select_by_value("10")

alloptions=dropdown.options
print("total no of options:",len(alloptions))