yas = int(input("Yaşınızı giriniz. "))

OkumaDurumu = input("Okuyor musunuz? (evet : e, hayır : h)")

if yas >= 18 and OkumaDurumu =="h":
    print("Askere gelme yaşınız geldi.")
    
elif yas >= 18 and OkumaDurumu == "e":
    print("okulunuz bittiğinde askere geleceksiniz!")
    
else: 
    print("daha askerlik yaşınız gelmedi")