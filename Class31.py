import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("chromedriver.exe")
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().download_and_install()))
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.NAME,"user-name").send_keys("standard_user")
time.sleep(5)
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
time.sleep(5)
driver.find_element(By.NAME,"login-button").click()
time.sleep(5)

# elements = driver.find_elements(By.CSS_SELECTOR,"div.pricebar button")
# for element in elements:
#     element.click()
# Navigation commands => back,forward,refresh

# time.sleep(10)
# driver.back()
# time.sleep(10)
# driver.forward()
# time.sleep(10)
# driver.refresh()
# time.sleep(10)
# # conditional commands
# element.is_enabled()
# element.is_selected()
# element.is_displayed()

time.sleep(10)
drp = Select(driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select"))
drp.select_by_visible_text("Price (low to high)")
# Actionchains => to perform mouse related events


time.sleep(30)