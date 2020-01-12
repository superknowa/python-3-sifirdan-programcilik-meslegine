import os,time
kullanicilar = dict()
kullanicilar = {"tosiba":123}
temizle = ("cls" if os.name == "nt" else "clear")
cevrimici_kullanici = False
def kayit_ol():
	kullanici_adi = input("Kullanıcı adı girin: ")
	os.system(temizle)
	mail = input("Mailinizi girin: ")
	os.system(temizle)

	if not kontrol(kullanici_adi):
		print("====Kullanıcı adı mevcut!====")
		time.sleep(1)
		os.system(temizle)
		return kayit_ol()

	sifre = input("Şifrenizi girin: ")
	sifre_o = input("Şifrenizi bir kez daha girin: ")


	if sifre != sifre_o:
		print("====Şifreler eşleşmedi!====")
		time.sleep(1)
		os.system(temizle)
		return kayit_ol()

	dosya = open("kullanicilar.txt","a")
	dosya.write(kullanici_adi)
	dosya.write(" ")
	dosya.write(sifre)
	dosya.write(" ")
	dosya.write(mail)
	dosya.write("\n")
	dosya.close()
	print("Kullanıcı kaydedildi.")
	input()


def kontrol(kullanici_adi):
	try:
		if kullanici_adi not in open("kullanicilar.txt","r").read():
			return True
		else:
			return False
	except FileNotFoundError:
		return True


def girisYap():
	global cevrimici_kullanici
	kullanici_adi = input("Kullanıcı adınızı girin: ")
	sifre = input("Şifrenizi girin: ")

	dosya = open("kullanicilar.txt","r")
	satirlar = dosya.readlines()
	cevrimici_kullanici = False
	for kullanici in satirlar:
		bolunmus = kullanici.split()
		bolunmus_k_adi = bolunmus[0]
		bolunmus_sifre = bolunmus[1]
		if kullanici_adi == bolunmus_k_adi and sifre == bolunmus_sifre:
			cevrimici_kullanici = kullanici_adi

	if cevrimici_kullanici:
		print("Hoşgeldin: ",kullanici_adi)
	else:
		print("Kullanıcı adı veya şifre yanlış!")
	input("Devam etmek için bir tuşa basın.")


if __name__== "__main__":
	while True:
		os.system(temizle)
		print("""

				[1] Kayıt Ol
				[2] Giriş Yap

			""")
		secim = int(input("Seçiminizi yapın: "))
		if secim == 1:
			os.system(temizle)
			kayit_ol()
		elif secim == 2:
			os.system(temizle)
			girisYap()











#Dosya işlemleri
#On fly if yapısı*
#import user defined module