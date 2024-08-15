import time
from selenium import webdriver

driver = webdriver.Chrome()  # this chrome method automatically download chrome specific driver
'''or we can use service class. first we need to download browser specific chrome driver and 
save it in our local then use the path where it save and pass the same in service class
service_obj=Service('chrome driver path')
driver=webdriver.Chrome(service_obj)'''
#driver.get("https://google.com")
driver.get('https://rahulshettyacademy.com/AutomationPractice')


time.sleep(5)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
