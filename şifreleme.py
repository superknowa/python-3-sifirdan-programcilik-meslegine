#Kapsamlı Şifreleme Uygulaması

import string
import os

alfabe= string.ascii_lowercase
max_karakter= len(alfabe)

temizle= ("cls" if os.name == "nt" else "clear")


def seçenekler():
	while True:
		os.system(temizle)
		seçenek= input("Ne yapmak istersin: ").lower()
		if seçenek in ("şifrele","şifreleme","şifreleme yap","şifreleme yapmak","şifreleme yapmak isterim"):
			şifreleme()
		elif seçenek in ("şifre çöz,şifreyi çöz"):
			şifre_çöz()
		else:
			print("Şifreleme yapmak için (%s) yazın, şifre çözmek için (%s) yazın." % ("şifrele","şifre çöz"))


def şifreleme():
	metin= input("Şifrelenecek metni girin: ").lower()
	şifreleme_anahtarı= şifrelemeAnahtarı()
	şifrelenmiş_metin= ""
	for karakter in metin:
		if karakter.isalpha():
			karakter_sıra_no= ord(karakter)
			karakter_sıra_no += şifreleme_anahtarı

			if karakter_sıra_no > ord("z"):
				karakter_sıra_no -= max_karakter

			elif karakter_sıra_no < ord("a"):
				karakter_sıra_no += max_karakter

			şifreli_karakter= chr(karakter_sıra_no)
			şifrelenmiş_metin += şifreli_karakter

		else:
			şifrelenmiş_metin += karakter
	os.system(temizle)
	print("%s kelimesinin %d anahtarıyla şifrelenmiş hali %s" % (metin,şifreleme_anahtarı,şifrelenmiş_metin))
	input("Devam etmek için bir tuşa basın")



def şifre_çöz():
	şifreli_metin= input("Çözülecek şifreli metni girin: ").lower()
	şifreleme_anahtarı= şifrelemeAnahtarı()
	çözülmüş_metin= ""
	for karakter in şifreli_metin:
		if karakter.isalpha():
			karakter_sıra_no= ord(karakter)
			karakter_sıra_no -= şifreleme_anahtarı

			if karakter_sıra_no > ord("z"):
				karakter_sıra_no -= max_karakter

			elif karakter_sıra_no < ord("a"):
				karakter_sıra_no += max_karakter

			çözülmüş_karakter= chr(karakter_sıra_no)
			çözülmüş_metin += çözülmüş_karakter
			
		else:
			çözülmüş_metin += karakter
	os.system(temizle)
	print("%s şifreli metnin %d anahtarıyla çözülmüş hali %s" % (şifreli_metin,şifreleme_anahtarı,çözülmüş_metin))
	input("Devam etmek için bir tuşa basın")



def şifrelemeAnahtarı():
	anahtar= int(input("Şifreleme anahtarı girin (1-%s):" % max_karakter))
	if anahtar >=1 and anahtar <= max_karakter:
		return anahtar
	else:
		return 1



if __name__ == "__main__":
	seçenekler()