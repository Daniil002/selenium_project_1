from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')


login = driver.find_element(By.CSS_SELECTOR, 'div.orangehrm-login-form input[name="username"]')
login.send_keys('Admin')


password = driver.find_element(By.CSS_SELECTOR, 'div.orangehrm-login-form input[name="password"]')
password.send_keys('admin123')

button = driver.find_element(By.CLASS_NAME, 'oxd-button')
button.click()

act_dashboard = driver.find_element(By.CLASS_NAME, 'oxd-topbar-header-breadcrumb-module')
act_dashboard = act_dashboard.text
print(act_dashboard)
exp_dashboard = 'Dashboard'

if act_dashboard == exp_dashboard:
    print('Test passed')
else:
    print('Test Failed')
    
    
driver.close()