#from selenium.webdriver.chrome import webdriver
from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//input[@type="search"]').send_keys('ber')
results = driver.find_elements(By.XPATH,"//div/div[@class='product']")
for item in results:
    item.find_element(By.XPATH,"div[@class='product-action']/button").click()
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
#wait = WebDriverWait(driver,5)
driver.find_element(By.CSS_SELECTOR,".promocode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)
#wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
wait.until(expected_conditions.text_to_be_present_in_element (By.CSS_SELECTOR,".promoInfo"),"Code applied ..!"))
print(driver.find_element(By.CSS_SELECTOR,'.promoInfo').text)






