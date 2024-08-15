from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice')
#time.sleep(5)
driver.implicitly_wait(2)
name = 'Neha'
#alert_ obj= driver.switch_to.alert
#alert_text= alert_obj.text
#radio buttons
radiobtns = driver.find_elements(By.XPATH, "//div[@id='radio-btn-example']/fieldset/label/input")
for i in radiobtns:
     if i.get_attribute('value') == 'radio1':
       i.click()
       time.sleep(5)
       assert i.is_selected()









