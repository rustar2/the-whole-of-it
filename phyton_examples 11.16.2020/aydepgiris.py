# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 01:20:21 2021

@author: BABA
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#from selenium import webdriver

# Github credentials


username = "kadi"
password = "sif"

# initialize the Chrome driver
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')


chrome_path = '/usr/bin/google-chrome-stable %U '
#webbrowser.get(chrome_path).open('https://aydep.ahievran.edu.tr/n/login')
# head to github login page



driver.get("https://aydep.ahievran.edu.tr/n/login")

driver.find_element_by_id("form2").send_keys(username)

driver.find_element_by_id("form4").send_keys(password)
# click login button
driver.find_element_by_name("login").click()


WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Kullanıcı adı ve/veya şifre geçersiz"
# get the errors (if there are)
errors = driver.find_elements_by_class_name("ui-pnotify-text")
# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
    
    
else:
    print("[+] Login successful")
    
    
    # close the driver
#driver.close()
