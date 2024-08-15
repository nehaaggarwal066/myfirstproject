from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# 2 types of waits are implicit and explicit
# Implicit wait is like a global timeout
#which is applied on every element in the fil- declare on top of script

driver= webdriver.chrome()
#or service_obj= Service('path of chrome driver'),  driver= webdriver.chrome(service_obj)
driver.get('https://rahulshettyacademy.com/AutomationPractice')
driver.implicit_wait(5)
# it will put MAX 5 sec wait to each element, if element appear
# before 5 seconds it will move to next element, so better than time.sleep(5)
#time.sleep(5) blindly wait for 5 sec for each element to appear



#explicit wait is put explicitly to a particular element which we know might take more time to appear
# instead of increasing the gloabl time out(i.e implicit wait), we put explicit wait for that element.
# if we increase global timeout that may create problem eg. if an element doesn't exist in an application and
# has problem , in that case implicit wait will wait for max time
#which is not a good practice, bcz we know that element will appear max in 5 sec,so why to wait for 15 sec



#Explicit wait is applied to a specific element  until the specific conditionn appears
# find elements method return a list and if non-empty list is returned then it is fine for implicit wait and
# if empty list is returned it will consider it as element not appeared


wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'.class')))




