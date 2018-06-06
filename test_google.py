from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get('https://www.google.com/')
time.sleep(5)
driver.quit()