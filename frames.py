from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.find_element(By.XPATH,"//button[@class='tox-notification__dismiss tox-button tox-button--naked tox-button--icon' ]").click()
driver.switch_to.frame("mce_0_ifr")# give either frame name or ID in input parameter
print(driver.find_element(By.XPATH,"//p").text)
#interview question!!!!!!!!!!!!!! how to switch back to window after work on frame
driver.switch_to.default_content()# this will switch back to browser window
