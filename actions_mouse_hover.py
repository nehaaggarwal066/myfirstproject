import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
#ActionChain class for mouse events
driver= webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice')
driver.implicitly_wait(3)
action = ActionChains(driver)
# syntax. Action_obj.method_name()
#action.context_click(driver.find_element(By.CSS_SELECTOR,"#mousehover"))   # for right click
#awlways use.perform at the end to perform that action
action.move_to_element(driver.find_element(By.CSS_SELECTOR,"#mousehover")).click().perform()

'''
#how to switch between windows or handle different windows in selenium
#we have to tell selenium to switch to diff window, let us see how to do that
#driver.switch_to(window_name)
how to get window name, use driver.window_handles will give all open windows list, you can access using index
'''
driver.find_element(By.CSS_SELECTOR,"#openwindow").click()
#window_handles will give name of all open windows in list form
windows_list = driver.window_handles
driver.switch_to.window(windows_list[1])
driver.find_element(By.XPATH,"//li[@class='nav-item']/a[text()='Courses']").click()

