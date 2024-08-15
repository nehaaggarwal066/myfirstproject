from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common import alert

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice')
#https://rahulshettyacademy.com/dropdownPractice/
#static dropdown and dynamic dropdown
# use select class to handle static dropdown
dropdown = Select(driver.find_element(By.CSS_SELECTOR,'#dropdown-class-example'))
#dropdown.select_by_index(2)
#dropdown.select_by_value('option3')
dropdown.select_by_visible_text('Option1')
time.sleep(3)
#dynamic dropdown we have to handle like checkboxes or radhio buttons
driver.find_element(By.XPATH,'//input[@placeholder="Type to Select Countries"]').send_keys('IND')
time.sleep(3)
countries = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']")
for country in countries:
    if country.text == 'India':
        country.click()
        time.sleep(2)
        break
#assert driver.find_element(By.XPATH,'//input[@placeholder="Type to Select Countries"]').text == 'India'
assert driver.find_element(By.XPATH,'//input[@placeholder="Type to Select Countries"]').get_attribute('value') == 'India'
