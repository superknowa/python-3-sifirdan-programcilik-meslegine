#Chat Uygulaması

import kullanıcıkayıt
from datetime import date





def kişiselMenü(kullanıcı_adı):
	while kullanıcıkayıt.çevrimiçi_kullanıcı:
		print("""

				[1] Arkadaş Listemi Getir
				[2] Arkadaş Ekle
				[3] Direk Mesaj Gönder
				[4] Mesaj Kutusu
				[5] Çıkış

			""")

		seçim= int(input("Seçiminizi girin: "))

		if seçim == 1:
			kullanıcıkayıt.os.system(kullanıcıkayıt.temizle)
			arkadaşListesi(kullanıcı_adı)
		elif seçim == 2:
			kullanıcıkayıt.os.system(kullanıcıkayıt.temizle)
			arkadaş= input("Eklemek istediğiniz arkadaşınızın kullanıcı adını girin: ")
			arkadaşEkle(ben=kullanıcı_adı,arkadaş=arkadaş)
		elif seçim == 3:
			kullanıcıkayıt.os.system(kullanıcıkayıt.temizle)
			arkadaş= input("Mesajın gönderileceği arkadaşınızın kulanıcı adını yazın: ")
			mesaj= input("Mesajınızı yazın: ")
			mesajGönder(ben=kullanıcı_adı,arkadaş=arkadaş,mesaj=mesaj,tarih=date.today())
		elif seçim == 4:
			kullanıcıkayıt.os.system(kullanıcıkayıt.temizle)
			mesajKutusu(kullanıcı_adı)
		elif seçim == 5:
			kullanıcıkayıt.os.system(kullanıcıkayıt.temizle)
			print("Çıkış yapılıyor...")
			kullanıcıkayıt.çevrimiçi_kullanıcı= False
			input("Kayıt menüsüne dönmek için bir tuşa basın")


def mesajKutusu(kullanıcı_adı):
	try:
		mesajvar= False
		dosya= open("mesajlar.txt","r")
		satırlar= dosya.readlines()
		for mesaj in satırlar:
			bölünmüş= mesaj.split("||")
			gönderen= bölünmüş[0]
			alıcı= bölünmüş[1]
			mesaj= bölünmüş[2]
			tarih= bölünmüş[3]
			if kullanıcı_adı == gönderen or kullanıcı_adı == alıcı:
				print("""

					Gönderen: {gönderici}   Alıcı: {alıcı}
					
					Tarih: {gönderim_tarihi}

					Mesaj: {mesaj}

					""".format(gönderici=gönderen,alıcı=alıcı,gönderim_tarihi=tarih,mesaj=mesaj))
				mesajvar= True
				print("="*80)
		if not mesajvar:
			print("Mesaj kutunuz boş")
	except FileNotFoundError:
		print("Hiç mesajınız yok üzülmeyin kimsenin mesajı yok zaten mesajlar dosyası bile yok.")
	input("Devam etmek için bir tuşa basın.")


def mesajGönder(**kwargs):
	dosya= open("mesajlar.txt","a")
	dosya.write(kwargs["ben"].lower())
	dosya.write("||")
	dosya.write(kwargs["arkadaş"].lower())
	dosya.write("||")
	dosya.write(kwargs["mesaj"])
	dosya.write("||")
	dosya.write(str(kwargs["tarih"]))
	dosya.write("\n")
	dosya.close()
	print("{ben} adlı kişi {arkadaş} adlı kullanıcıya mesaj gönderdi.".format(ben=kwargs["ben"].title(),arkadaş=kwargs["arkadaş"].title()))
	input("Devam etmek için bir tuşa basın.")


def arkadaşEkle(**kwargs):

	dosya= open("arkadaşlıklar.txt","a")
	dosya.write(kwargs["ben"].lower())
	dosya.write(" ")
	dosya.write(kwargs["arkadaş"].lower())
	dosya.write("\n")
	dosya.close()
	print("{ben} isimli kişi {arkadaş} isimli kullanıcıyı arkadaş olarak ekledi.".format(ben=kwargs["ben"].title(),arkadaş=kwargs["arkadaş"].title()))
	input("Devam etmek için bir tuşa basın.")

def arkadaşListesi(kullanıcı_adı):
	try:
		arkadaşvar= False
		dosya = open("arkadaşlıklar.txt","r")
		satırlar= dosya.readlines()
		for arkadaşlıklar in satırlar:
			bölünmüş= arkadaşlıklar.split()
			ark_1= bölünmüş[0]
			ark_2= bölünmüş[1]
			if kullanıcı_adı == ark_1:
				print(ark_2)
				arkadaşvar= True
			elif kullanıcı_adı == ark_2:
				print(ark_1)
				arkadaşvar= True
		if not arkadaşvar:
			print("Hiç arkadaşın yok ama üzülme senin de olacak.")
	except FileNotFoundError:
		print("Hiç arkadaşın yok üzülme bu programda kayıtlı kimsenin yok çünkü daha arkadaşlıklar dosyası bile yok")
	input("Devam etmek için bir tuşa basın.")








if __name__=="__main__":
	while True:
		kullanıcıkayıt.os.system(kullanıcıkayıt.temizle)
		print("""

				[1] Kayıt Ol
				[2] Giriş Yap



			""")

		seçim= int(input("Seçiminizi girin: "))

		if seçim == 1:
			kullanıcıkayıt.os.system(kullanıcıkayıt.temizle)
			kullanıcıkayıt.kayıt_ol()
		elif seçim == 2:
			kullanıcıkayıt.os.system(kullanıcıkayıt.temizle)
			kullanıcıkayıt.giriş_yap()


			if kullanıcıkayıt.çevrimiçi_kullanıcı:
				kişiselMenü(kullanıcıkayıt.çevrimiçi_kullanıcı)