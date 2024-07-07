import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
action_chain_object = ActionChains(driver)

driver.get('https://testffc.nimapinfotech.com/')
driver.implicitly_wait(20)
#driver.maximize_window()

#Login Journey

driver.find_element('xpath', '//input[@id="mat-input-0"]').send_keys('samk4723@outlook.in')
time.sleep(3)
driver.find_element('xpath', '//input[@id="mat-input-1"]').send_keys('Shubham@nimap')
time.sleep(3)

Captcha_input = input("Please enter the CAPTCHA manually and press Enter to continue...")

driver.find_element('xpath', '//input[@formcontrolname="captchaValue"]').send_keys(Captcha_input)
time.sleep(2)
driver.find_element('xpath', '//button[@id="kt_login_signin_submit"]').click()
time.sleep(10)

#Verify the Toast/Popup message after the PunchIn


driver.find_element('xpath','//button[@class="buttonData punchBtn mat-raised-button mat-button-base mat-primary"]//span[text()="Punch In"]').click()
driver.switch_to_alert().accept


# Add Customer

driver.find_element('xpath', '//span[text() ="My Customers"]').click()
time.sleep(1)
driver.find_element('xpath', '//span[text()=" New Customer "]').click()
time.sleep(10)
driver.find_element('xpath','//input[@id="mat-input-14"]').send_keys('shubham kumar')
time.sleep(3)
driver.find_element('xpath','//input[@id="mat-input-16"]').send_keys('Avinash kumar')
time.sleep(3)
driver.find_element('xpath','//input[@id="mat-input-17"]').send_keys('7272941238')
time.sleep(3)
driver.find_element('xpath','//input[@id="mat-input-19"]').send_keys('it1912avi@gmail.com')
driver.implicitly_wait(20)
driver.find_element('xpath','//input[@ng-reflect-placeholder="Address"]').click()
driver.implicitly_wait(20)
driver.find_element('xpath','//button[@class="float-right mat-raised-button mat-button-base mat-primary"]').click()
time.sleep(10)
driver.find_element('xpath','//input[@ng-reflect-placeholder="Pincode"]').send_keys('560043')
time.sleep(5)
driver.find_element('xpath','//button[@ng-reflect-message="Save changes"]').click()
time.sleep(10)





