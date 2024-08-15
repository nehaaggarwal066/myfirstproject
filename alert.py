import time
from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # this chrome method automatically download chrome specific driver
driver.get('https://rahulshettyacademy.com/AutomationPractice')
#alert example:
driver.find_element(By.XPATH,"//input[@id='name']").send_keys('Neha')
#driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
alert_obj=driver.switch_to.alert
time.sleep(2)
alert_txt= alert_obj.text
print(alert_txt)
#to accept alert
#alert_obj.accept()
#to reject alert
alert_obj.dismiss()
print(driver.find_elements(By.LINK_TEXT,"https"))


