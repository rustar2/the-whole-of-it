from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
from datetime import datetime
import time
import os


now = datetime.now() # zaman degiskenlerimiz cekicez ay yıl vd

#FONKOSYONLAR#
def mlzme(x):#Malzeme Bilimi
    print("Malzeme Bİlimi")
    #driver.get('https://aydep.ahievran.edu.tr/n/lesson-categories-weekly/287529')
    drss=   [0,15,15]
    drsd=   [0,6,56]
    return drss , drsd
def bl1(x):#C Dersi
    print("C dersi")
    #driver.get('https://aydep.ahievran.edu.tr/n/lesson-categories-weekly/287851')
    drss=   [0,18,19]
    drsd=   [0,26,16]
    return drss , drsd
    
def mat(x):#Mühendislik Matemeatigi
    print("Mühendislik Matemeatigi")
    #driver.get('https://aydep.ahievran.edu.tr/n/lesson-categories-weekly/287501')
    drss=   [0,14,15]
    drsd=   [0,16,6]
    return drss , drsd
    
def mkvm(x):#Mukavemet
    print("Mukavemet")
    #driver.get('https://aydep.ahievran.edu.tr/n/lesson-categories-weekly/287543')
    drss=   [0,16,17]
    drsd=   [0,46,36]
    return drss , drsd
    
def termo(x):#Termodinamik
    print("Termodinamik")
    #driver.get('https://aydep.ahievran.edu.tr/n/lesson-categories-weekly/287515')
    drss=   [0,17,18]
    drsd=   [0,36,26]
    return drss , drsd
    
def emt(x):#Em Temelleri
    print("Em Temelleri")
    #driver.get('https://aydep.ahievran.edu.tr/n/lesson-categories-weekly/287557')
    drss=   [0,10,00]
    drsd=   [0,6,00]
    return drss , drsd
    
def day_of_week(year, month, day):
	t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
	year -= month < 3
	return (year + int(year/4) - int(year/100) + int(year/400) + t[month-1] + day) % 7


##############degiskenlerın tanımlanması##########################

yıl =   int(now.strftime("%Y"))
ay  =   int(now.strftime("%m"))
gün =   int(now.strftime("%d"))
dkk =   int(now.strftime("%M"))
saat=   int(now.strftime("%H"))
y=0
dngu=1
a=1
drs1= [0,0,0]
drs2= [0,0,0]
drs3= [0,0,0]

## ayın gününün belirlenmesı ve ders ismlerının ve saatlerının alınması ##
gnlr=int(day_of_week(yıl,ay,gün))
if gnlr == 1:
    print("Pazartesi")
    drs1=emt(y)
    drs2=mat(y)
    drs3=termo(y)
    print("1.ders1 saati:",drs1[0][1],drs1[1][1],"2.saati :",drs1[0][2],drs1[1][2])
    print("2.ders1 saati:",drs2[0][1],drs2[1][1],"2.saati :",drs2[0][2],drs2[1][2])
    print("3.ders1 saati:",drs3[0][1],drs3[1][1],"2.saati :",drs3[0][2],drs3[1][2])
    
elif gnlr == 2 :
    print("Salı")
    drs1=mlzme(y)
    drs2=mkvm(y)
    print("1.ders1 saati:",drs1[0][1],drs1[1][1],"2.saati :",drs1[0][2],drs1[1][2])
    print("2.ders1 saati:",drs2[0][1],drs2[1][1],"2.saati :",drs2[0][2],drs2[1][2])
    
elif gnlr == 3:
   # print("Çarsamba")
    print("Bügün ders yok.")
elif gnlr == 4:
    print("Persembe")
    drs1=bl1(y)
    print("1.ders1 saati:",drs1[0][1],drs1[1][1],"2.saati :",drs1[0][2],drs1[1][2])
    
elif gnlr == 5 : 
    #print("Cuma")
    print("Bügün ders yok.")
else:
    print("Bügün ders yok.")

print("time:", saat , dkk ,ay,yıl,gün)




"""
while a == 1:
##################  gostergecler ve ekran #############################
#######################################################################
    now = datetime.now()
    dkk =   int(now.strftime("%M"))
    saat=   int(now.strftime("%H"))
    dngu=dngu+1
    if dngu == 100:
        dngu=1
    print("Ders Saati Bekleniyor\n","="*dngu)
    time.sleep( 1 )
    os.system("clear")
    
#######################################################################
#######################################################################
    #####1 ders sorgusu 1.saat######
    if drs1[0][1] == saat:
        if drs1[1][1]== dkk:
            os.system("clear")
            print("gumbur gumbur gelıyozz")
            a=a+1
            
    #####1 ders sorgusu 2.saat #####
    if drs1[0][2] == saat:
        if drs1[1][2]== dkk:
            os.system("clear")
            print("gumbur gumbur gelıyozz")
            a=a+1
            
#######################################################################
#######################################################################
            
    #####2 ders sorgusu 1.saat######
    if drs2[0][1] == saat:
        if drs2[1][1]== dkk:
            os.system("clear")
            print("gumbur gumbur gelıyozz")
            a=a+1
    #####2 ders sorgusu 2.saat #####
    if drs2[0][2] == saat:
        if drs2[1][2]== dkk:
            os.system("clear")
            print("gumbur gumbur gelıyozz")
            a=a+1
            
#######################################################################
#######################################################################

    #####3 ders sorgusu 1.saat######
    if drs3[0][1] == saat:
        if drs3[1][1]== dkk:
            os.system("clear")
            print("gumbur gumbur gelıyozz")
            a=a+1
    #####3 ders sorgusu 2.saat #####
    if drs3[0][2] == saat:
        if drs3[1][2]== dkk:
            os.system("clear")
            print("gumbur gumbur gelıyozz")
            a=a+1




"""
"""

usr=('13936156420')  
pwd=('13936156420')  
  
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://aydep.ahievran.edu.tr/n/login') 
 
  
username_box = driver.find_element_by_id('form2') 
username_box.send_keys(usr) 

 
  
password_box = driver.find_element_by_id('form4') 
password_box.send_keys(pwd) 

  
giris = driver.find_element_by_name('login') 
giris.click()




mlzme()
senkron = driver.find_element_by_name('senkron') 
senkron.click()

driver.get('https://aydep.ahievran.edu.tr/n/lesson-categories-weekly/287529/senkron/75947/join')


"""






#driver.quit()
