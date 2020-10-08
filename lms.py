from selenium import webdriver
browser  = webdriver.Safari()


browser.get('http://lms.sicsr.ac.in/login/index.php')
browser.fullscreen_window()
#Fill user id
browser.find_element_by_css_selector('#username').send_keys('PRN')
browser.find_element_by_css_selector('#password').send_keys('psw')
browser.find_element_by_css_selector('#loginbtn').click()


