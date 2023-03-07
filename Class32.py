import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()

# driver.get("https://demo.guru99.com/test/newtours/register.php")
# time.sleep(10)
# actions = ActionChains(driver)
# element = driver.find_element(By.XPATH,"//a[@class='dropdown-toggle'][normalize-space()='Selenium']")
# actions.move_to_element(element).click().perform()
# time.sleep(5)
# element = driver.find_element(By.XPATH,"//a[normalize-space()='Ajax Demo']")
# actions.move_to_element(element).click().perform()
# time.sleep(30)

driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)
# time.sleep(10)
# actions = ActionChains(driver)
# sourceelement = driver.find_element(By.XPATH,"//div[@id='draggable']")
# targetelement = driver.find_element(By.XPATH,"//div[@id='droppable']")
# actions.drag_and_drop(sourceelement,targetelement).perform()
# time.sleep(10)
#
# element = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
# # actions.context_click(element).perform()
# time.sleep(10)
# actions.double_click(element).perform()
# time.sleep(20)
# driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
# time.sleep(10)
# driver.switch_to.alert.accept()
# time.sleep(10)
# driver.find_element(By.XPATH,"//button[@onclick='myFunction()']").click()
# time.sleep(10)
# driver.switch_to.alert.dismiss()

# till some pixel
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(10)
# element = driver.find_element(By.XPATH,"//div[@id='slider']")

# till into some view
# driver.execute_script("arguments[0].scrollIntoView();",element)

#till end
# time.sleep(10)
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(10)


# Asynchronous
# Synchronous

# Wait concepts
# Implicit wait => this will add at the page level , and this is called dynamic wait , it will wait till
# all elements to load with in the time provided
# Explicit wait => this is for particular element based on expected condition

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

#
# wait = WebDriverWait(driver,10,3)
# element = wait.until(ec.visibility_of_element_located(By.ID,"txt1"))
# element.click()

# how will take screenshot
driver.save_screenshot("sample.jpg")

driver.close() # it will close the current tab
driver.quit() # it will close the complete window with all tabs
