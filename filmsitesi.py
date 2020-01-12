yas_limiti = 18
izleyicinin_yasi = int(input("Lütfen yaşınızı girin: "))

if izleyicinin_yasi<yas_limiti:
	print("Bu film korku öğeleri içerir.Yaşınız tutmuyor.")
elif izleyicinin_yasi>80:
	print("Kalp hastalığınız varsa bu filmi izlemeniz önerilmez.")
else:
	print("İyi seyirler")
