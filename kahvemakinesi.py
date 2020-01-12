seker = input("Şeker kullanıyor musunuz?: ")

secim = int(input("İçecek numaranızı girin: "))

if seker:
    if secim == 1:
        if seker == "evet":
            print("Şeker Atılıyor")
        elif seker == "hayır":
            print("Şeker Atılmadı")
        print("Filtre kahveniz hazırlanıyor.")  
    elif secim == 2:
         if seker == "evet":
            print("Şeker Atılıyor")
         elif seker == "hayır":
            print("Şeker Atılmadı") 
         print("Espressonuz hazırlanıyor.")
    elif secim == 3:
        if seker == "evet":
            print("Şeker Atılıyor")
        elif seker == "hayır":
            print("Şeker Atılmadı")
        print("Sıcak çikolatanız.")
    elif secim == 4:
        if seker == "evet":
            print("Şeker Atılıyor")
        elif seker == "hayır":
            print("Şeker Atılmadı")
        print("Mochanız hazırlanıyor.")
    else:
        print("Menüde olmayan bir numara girdiniz.")
else:
    print("Şeker tercihi girilmemiş")
