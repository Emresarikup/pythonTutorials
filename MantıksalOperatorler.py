ehliyet = False 
araba = True

if ehliyet and araba:
    print("Araba kullanabilirsin")
    
    
elif araba and not ehliyet:
    print("Bizim sürücü kursumuzu tercih ederek hemen araba kullanmaya başlayabilirsin")
    

elif ehliyet or araba:
    print("Araba kullanmana çok az kaldı")
    
    
else:
    print("Araba kullanman için çok zaman var.")