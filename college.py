#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
l = sys.argv

browser = webdriver.Safari()
browser.get('https://gmail.com')
browser.fullscreen_window()
#Fill user id
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('email')
time.sleep(1)
emailElem.send_keys(Keys.RETURN)
time.sleep(1)
passwordElem = browser.find_element_by_name('password').send_keys('psw')
browser.find_element_by_css_selector('#passwordNext > span:nth-child(3) > span:nth-child(1)').click()



