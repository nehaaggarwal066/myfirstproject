from selenium import webdriver
from selenium.webdriver.common.by import By

#How to open run test in headless mode:
Chromeoptions_obj= webdriver.ChromeOptions()
#Chromeoptions_obj.add_argument("headless")

#How to ignore certification related errors
Chromeoptions_obj.add_argument("--ignore_certificate-errors")

#maximize mode
Chromeoptions_obj.add_argument("--start-maximized")

#pass this object when you call webdriver.Chrome() as argument
driver = webdriver.Chrome(options = Chromeoptions_obj)
driver.get('https://rahulshettyacademy.com/AutomationPractice')

print(driver.title)

#how to scroll a webpage or how to embedd javascript in selenium- use .execute_script method
# use this method always wo write any java script code :driver.execute_script("put script here")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


# how to take screenshots
driver.get_screenshot_as_file("scree.png")


# how to print all links of a web page
tags = driver.find_elements(By.XPATH,"//a")
length = len(tags)
print(length)
for i in tags :
    print(i.text)

tag1 = driver.find_elements(By.)
print(len(tag1))
