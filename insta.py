from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#chrome = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path = '/Users/binary/chromedriver 2')
driver.get('https://www.instagram.com/')
time.sleep(3)
#search_box = driver.find_element_by_name('q')
#search_box.send_keys('test')
#search_box.submit()
un = ''
pw = ''
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
username.send_keys(un)
password.send_keys(pw)
time.sleep(3)
loginButton = driver.find_element(By.CLASS_NAME, 'L3NKy')
loginButton.click()
time.sleep(6)
saveButton = driver.find_element(By.CLASS_NAME, 'cmbtv')
saveButton.click()
time.sleep(3)