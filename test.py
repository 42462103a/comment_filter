from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://www.google.com/maps/@23.4857501,119.4996499,7z?authuser=0&entry=ttu")
driver.switch_to.active_element.send_keys("龍德小館")
driver.switch_to.active_element.send_keys(Keys.RETURN)
buttons = driver.find_elements(By.CLASS_NAME, "hh2c6")

buttons[1].click()
driver.implicitly_wait(2)
scroll = driver.find_element(By.CLASS_NAME,"m6QErb.DxyBCb.kA9KIf.dS8AEf")


