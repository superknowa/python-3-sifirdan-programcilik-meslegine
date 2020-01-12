#İngilizce-Türkçe Sözlük
import os



kelimeler = {
	

	"get":["Almak","Edinmek","Olmak","Elde etmek"],
	"break":["Mola","Ara","Kırılma","Fren"],
	"winner":["Kazanan","Galip","Birinci"]



}

def kelimeEkle(kelime,kelimeler):
	if kontrol(kelime,kelimeler):
		mevcut_anlamlar = set(kelimeler[kelime])
		yeni_giriş= input("Kelime zaten mevcut. Girdiğiniz kelimenin kayıtlı anlamları: {}\n Yeni bir anlam girmek ister misiniz?(E/H)".format(mevcut_anlamlar))
		if yeni_giriş.lower()=="e":
			yeni_anlamlar= input("Girmek istediğiniz anlamları aralarına virgül koyarak yazın: ")
			yeni_anlamlar_bölünmüş= set(yeni_anlamlar.split(","))
			kelimeler[kelime]= list(mevcut_anlamlar | yeni_anlamlar_bölünmüş)
			print("Girdiğiniz anlamlar kaydedildi. Anlamlar listesinin son hali: ",kelimeler[kelime])
		elif yeni_giriş.lower() == "h":
			pass
	else:
		yeni_anlamlar= input("Girmek istediğiniz anlamları aralarına virgül koyarak yazın: ")
		yeni_anlamlar_bölünmüş= set(yeni_anlamlar.split(","))
		kelimeler[kelime]= list(yeni_anlamlar_bölünmüş)
		print("Girdiğiniz anlamlar kaydedildi. Anlamlar listesinin son hali: ",kelimeler[kelime])
	input("Devam etmek için bir tuşa basın.")



def kelimeÇevir(kelime,kelimeler):
	if kontrol(kelime,kelimeler):
		print("{} kelimesinin anlamları ".format(kelime),end=": ")
		print(*kelimeler[kelime])
	else:
		print("Girdiğiniz kelime mevcut değildir.")
	input("Devam etmek için bir tuşa basın.")



def kontrol(kelime,kelimeler):
	if kelime in kelimeler:
		return True
	else:
		return False



def kelimeleriListele():
	for no,kelime in enumerate(kelimeler,1):
		print("{}.{}".format(no,kelime))
	input("Devam etmek için bir tuşa basın.")




secenekler= """

	[1] Kelime Ekle
	[2] Kelime Çevir
	[3] Kelimeleri Listele


"""

while True:
	temizle= ("cls" if os.name == "nt" else "clear")
	os.system(temizle)
	print(secenekler)
	secenek= int(input("Seçiminizi yapın: "))

	if secenek == 1:
		kelime= input("Eklenecek ingilizce kelimeyi girin: ")
		kelimeEkle(kelime,kelimeler)
	elif secenek == 2:
		kelime= input("Anlamını öğrenmek istediğiniz kelimeyi girin: ")
		kelimeÇevir(kelime,kelimeler)
	elif secenek == 3:
		kelimeleriListele()
