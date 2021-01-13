# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:02:32 2020

@author: BABA
"""

from mechanize import Browser
from bs4 import BeautifulSoup
import requests
import random
import webbrowser
l="31543115193115614985586481413148646443125884824346459318649348364592950315720"

print(len(str(l)),"uzunluk")
u=len(str(l))
k=""
a=0
for i in range(a,u,1): 
    l=random.randint(0,9)
    print(l,end="")
    k=k+str(l)
    a=a+1
    
  

    #Zorlama assada
b="https://obs.ahievran.edu.tr/oibs/zfoto.aspx?gkm="
print("",end="\n")


url = (b+k)



# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

webbrowser.get(chrome_path).open(url)

  # Url nin titleinden resim boyutu çekiyoruz
# target url 
url = 'https://obs.ahievran.edu.tr/'
# creating a Browser instance 
br = Browser() 
br.open(url) 
  
# displaying the title 
print("Title of the website is : ") 
print( br.title())
print(len("72144724444844032487461146836044412050484453643015904915187493530144423324854080"))
