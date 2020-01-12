#Hesap Makinesi

secenek= """

		[1] Toplama [2] Çıkarma [3] Çarpma [4] Bölme [5] Üs Alma


"""
print(secenek)

secenek= int(input("Seçiminizi yapın: "))
sayılar= input("İşlem yapılacak sayıları aralarında birer boşluk bırakarak girin: ")
sayılar_bölünmüş= sayılar.split(" ")

if secenek == 1:
	ilk_sayı= float(sayılar_bölünmüş[0])
	ikinci_sayı= float(sayılar_bölünmüş[1])

	print("{} + {} = {}".format(ilk_sayı,ikinci_sayı,ilk_sayı + ikinci_sayı))

elif secenek == 2:
	ilk_sayı= float(sayılar_bölünmüş[0])
	ikinci_sayı= float(sayılar_bölünmüş[1])

	print("{} - {} = {}".format(ilk_sayı,ikinci_sayı,ilk_sayı - ikinci_sayı))

elif secenek == 3:
	ilk_sayı= float(sayılar_bölünmüş[0])
	ikinci_sayı= float(sayılar_bölünmüş[1])

	print("{} * {} = {}".format(ilk_sayı,ikinci_sayı,ilk_sayı * ikinci_sayı))

elif secenek == 4:
	ilk_sayı= float(sayılar_bölünmüş[0])
	ikinci_sayı= float(sayılar_bölünmüş[1])

	print("{} / {} = {}".format(ilk_sayı,ikinci_sayı,ilk_sayı / ikinci_sayı))

elif secenek == 5:
	ilk_sayı= float(sayılar_bölünmüş[0]) #Taban
	ikinci_sayı= int(sayılar_bölünmüş[1]) #Kuvvet

	print("{} ** {} = {}".format(ilk_sayı,ikinci_sayı,ilk_sayı ** ikinci_sayı))
else:
	print("Hatalı bir seçim yaptınız")
