# Selenium-webdriver

Selenium WebDriver is a code library of APIs for controlling browsers.

## Installation

Use the package manager (pypi.org/project/selenium/4.0.0.b4/) to install selenium stable version and for install chrome driver use (https://chromedriver.chromium.org/downloads).

## Usage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj=Service("D:\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# count no of rows and columns
noofrows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
noofcolumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(noofrows,noofcolumns)

# read specific row and column data
cover=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(cover)

# read for all rows and columns
print("printing all the rows and columns")

for r in range(2,noofrows+1):
    for c in range(1,noofcolumns+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end='            ')
    print()


# read data based on condition
for r in range(2,noofrows+1):
    authorname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorname=="Mukesh":
       bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
       print(bookname,"       ",authorname)

driver.close()

## Description

Here I'm taking ("https://testautomationpractice.blogspot.com/") website to take the data of book name, author name and price of certain books respectively.
Here we also particularly mention the row number and column number to get the details of certain author and whose their book name and price. To get these details we used the x-path of that element.



