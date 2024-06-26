ilkSayi = int(input("ilk sayıyı giriniz "))
İkinciSayi = int(input("ikinci sayıyı giriniz "))

islem = input("""Yapmak istediğiniz işlemi giriniz.
Toplama : + , çıkarma : - , çarpma: x , bölme : /            
""")

if islem == "+":
    print("sonuç: " + str(ilkSayi + İkinciSayi))
    

elif islem == "-":
    print("sonuç: " + str(ilkSayi - İkinciSayi))
    
    
elif islem == "x":
    print("sonuç: " + str(ilkSayi * İkinciSayi))
    
    
elif islem == "/":
    print("sonuç: " + str(ilkSayi / İkinciSayi))