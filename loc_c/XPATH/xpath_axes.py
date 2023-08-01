from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("D:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()
#
# self=driver.find_element(By.XPATH,"//a[contains(.,'Zensar Technologies')]/self::a").text
# print(self)
#
# parent=driver.find_element(By.XPATH,"//a[contains(.,'Zensar Technologies')]/parent::td").text
# print(parent)
#
# childs=driver.find_elements(By.XPATH,"//a[contains(.,'Jyothy Labs')]/ancestor::tr/child::td")
# print(len(childs))
#
# ancestor=driver.find_element(By.XPATH,"//a[contains(.,'Jyothy Labs')]/ancestor::tr").text
# print(ancestor)
#
# descendants=driver.find_elements(By.XPATH,"//a[contains(.,'Jyothy Labs')]/ancestor::tr/descendant::*")
# print("Number of descendant nodes:",len(descendants))
#
# followings=driver.find_elements(By.XPATH,"//a[contains(.,'Jyothy Labs')]/ancestor::tr/following::*")
# print("Number of following nodes:",len(followings))

#followingsiblings=driver.find_elements(By.XPATH,"//a[contains(.,'Jyothy Labs')]/ancestor::tr/following-sibling::*")
#print("Number of following nodes:",len(followingsiblings))

#precedings=driver.find_elements(By.XPATH,"//a[contains(.,'Jyothy Labs')]/ancestor::tr/preceding::*")
#print("Number of following nodes:",len(precedings))

precedingsiblings=driver.find_elements(By.XPATH,"//a[contains(.,'Jyothy Labs')]/ancestor::tr/preceding-sibling::*")
print("Number of following nodes:",len(precedingsiblings))
