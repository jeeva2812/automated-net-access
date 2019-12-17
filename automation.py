#!/usr/bin/env python3

'''
Author: jeeva2812
'''

#Change this
rollNo = 'roll number'
pwd = 'password'

import selenium
import selenium.webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless") #Remove this to see the process
driver = selenium.webdriver.Chrome(options=chrome_options)

driver.get('https://netaccess.iitm.ac.in/account/login')

rollNo_box = driver.find_element_by_id('username')
rollNo_box.send_keys(rollNo)

pwd_box = driver.find_element_by_id('password')
pwd_box.send_keys(pwd)

login_button = driver.find_element_by_id('submit')
login_button.click()

driver.get('https://netaccess.iitm.ac.in/account/approve')

oneDay = driver.find_element_by_id('radios-1')
oneDay.click()

approve_button = driver.find_element_by_id('approveBtn')
approve_button.click()

#print("Successfully authenticated")
