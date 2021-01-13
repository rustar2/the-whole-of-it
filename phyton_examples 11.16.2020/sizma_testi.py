# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 00:51:45 2020

@author: BABA
"""

"""import requests
cekis=requests.get()
a=cekis.content
print (a)

print(cekis)"""


import requests
import random
import webbrowser


l="72144724444844032487461146836044412050484453643015904915187493530144423324854080"



b="https://obs.ahievran.edu.tr/oibs/zfoto.aspx?gkm=0"

print("cuka")


u=len(str(l))
k=""
knt=3882
dongu=0

while knt==3882:
    k=""
   # print("sa")
    a=0
    print("attending")
    for i in range(a,u,1): 
        l=random.randint(0,9)
      # 
        k=k+str(l)
        a=a+1
    print("",end="\n")    
    
    url = (b+k)
    response=requests.get(url)
    z=len(response.content)
    knt=z
    dongu=dongu+1
    print(dongu)
    
    


print(url)
print("",end="\n")

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

webbrowser.get(chrome_path).open(url)


     
