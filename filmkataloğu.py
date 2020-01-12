#Film Kataloğu(Detaylı Arama)
from os import system

filmler= [
		("Kara Korsanın Laneti",1957,8.2,"Korku"),
		("Sineğin İntikamı",2957,1.2,"Belgesel"),
		("Yılan Rüzgarı",1997,9.2,"Romantik")
]


def filmleriListele(filtre=None,değer=None):
	system("cls")
	print("\n")
	for film in filmler:
		if not filtre and not değer:
			print("Filmin adı: {}({})-----Imdb: {}-------Tür: {}".format(film[0],film[1],film[2],film[3]))
		elif filtre == "Film Adı":
			if değer.lower() == film[0].lower():
				print("Filmin adı: {}({})-----Imdb: {}-------Tür: {}".format(film[0],film[1],film[2],film[3]))
		elif filtre == "Yapım Yılı":
			if değer == film[1]:
				print("Filmin adı: {}({})-----Imdb: {}-------Tür: {}".format(film[0],film[1],film[2],film[3]))
		elif filtre == "Imdb":
			if değer == film[2]:
				print("Filmin adı: {}({})-----Imdb: {}-------Tür: {}".format(film[0],film[1],film[2],film[3]))
		elif filtre == "Tür":
			if değer.lower() == film[3].lower():
				print("Filmin adı: {}({})-----Imdb: {}-------Tür: {}".format(film[0],film[1],film[2],film[3]))
	print("\n")
	input("Devam etmek için bir tuşa basın")



menü = """


		Filmi hangi kıstasa göre aramak istersiniz?

		[1] Film Adı
		[2] Yapım Yılı
		[3] Imdb Puanı
		[4] Türü
		[5] Hepsini Getir
		[0] Çıkış Yap


"""

while True:

	print(menü)

	seçim= int(input("Seçiminizi yapın: "))


	if seçim == 1:
		mesaj = "Film adını girin: "
		filtre = "Film Adı"
	elif seçim == 2:
		mesaj = "Yapım yılını girin: "
		filtre = "Yapım Yılı"
	elif seçim == 3:
		mesaj = "Imdb puanını girin: "
		filtre = "Imdb"
	elif seçim == 4:
		mesaj = "Film türünü girin: "
		filtre = "Tür"


	if seçim == 1 or seçim == 4:
		değer = input(mesaj)
		filmleriListele(filtre,değer)
	elif seçim == 2:
		değer = int(input(mesaj))
		filmleriListele(filtre,değer)
	elif seçim == 3:
		değer = float(input(mesaj))
		filmleriListele(filtre,değer)
	elif seçim == 5:
		filmleriListele()
	elif seçim == 0:
		quit()