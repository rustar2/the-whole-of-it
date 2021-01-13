def kulsifControl():
    control=False
    controlsif=False
    while not control:
        kadi=input("kullanıcı adı giriniz: ")
        harfler=("safabababurda")
        sifreler="1234567890"
        if len(kadi)<=13:
            a=0
            for olc in kadi:
                if olc in harfler:
                     a=a+1
            if a==len(kadi):
                print("Doğru kullanıcı adı")
                control=True
                while not controlsif:
                    sifre=input("Şifreyi Giriniz: ")
                    while not controlsif:
                        if len(sifre)<13:
                            b=0
                            for sifolc in sifre:
                                    if sifolc in sifreler:
                                        b=b+1
                            if b==len(sifre):
                                controlsif=True
                                print("Sifre tamam")
                                print("Şifreniz :{}  Kullanıcı Adınız :{}".format(sifre,kadi))
                                
                            else:print("sifre yanlıs")
                    
                        
            else:print("Kullanıcı adınız Yanlış")
        else:print("Kullanıcı adı 13 karakterden fazla olamaz")
    return kadi
calistir=kulsifControl()