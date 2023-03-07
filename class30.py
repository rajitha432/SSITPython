import time

# Pytest
# UI => Selenium
# Selenium => UI Testing Framework => we can test only web applications
# Page object model framework => The page( DOM => document object model)will be accessed through an object
# with same object will perform all UI actions
# webdriver => controlling the webpage , by using this we will perform all UI actions
#

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdrivermanager.chrome import ChromeDriverManager


driver = webdriver.Chrome("chromedriver.exe")
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().download_and_install()))
driver.get("https://www.saucedemo.com/")
driver.maximize_window()


# locators/selectors  => to identify the element
# Id =>
# Name =>
# ClassName=>
# Css Selector =>
# XPath => Absolute Path/Relative Path => it works with parent and child hierarchy
# Absolute Path => it will indicate with single slash / , it will navigate from root of html page , that is html element
# ex : html/body/div[5]/div[1]/div/h4[1]
# Relative Path => it will indicate with double slash // , it will try to find element from particular element
# //div[@class='col-md-3'][1]/div/ul[1]/li[1]
# LinkText=>
# PartialLinktext=>

# driver.find_element(By.ID,"user-name").send_keys("standard_user")
# time.sleep(5)
# driver.find_element(By.ID,"password").send_keys("secret_sauce")
# time.sleep(5)
# driver.find_element(By.ID,"login-button").click()

driver.find_element(By.NAME,"user-name").send_keys("standard_user")
time.sleep(5)
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
time.sleep(5)
driver.find_element(By.NAME,"login-button").click()
time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"button#add-to-cart-sauce-labs-backpack").click()
elements = driver.find_elements(By.CSS_SELECTOR,"div.pricebar button")
for element in elements:
    element.click()

driver.find_element(By.LINK_TEXT,"Gmail")
driver.find_element(By.PARTIAL_LINK_TEXT,"Imag")
time.sleep(30)

# find_element => it will find exact one element and if element not found it will give NoSuchelement exception
# find_elements => it will give list of elements which has same locator

