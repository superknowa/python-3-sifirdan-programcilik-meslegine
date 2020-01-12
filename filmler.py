filmler= {
	
	"Kara Korsanın Laneti":{"Yapım Yılı":1957,"Imdb":8.2,"Tür":"Korku"},
	"Sineğin İntikamı":{"Yapım Yılı":2957,"Imdb":1.2,"Tür":"Belgesel"}

}


def filmEkle():
	film_adı = input("Film adı girin: ")
	global filmler

	if film_adı:
		yapım_yılı = input("Yapım yılını girin: ")
		imdb = input("İmdb puanını girin: ")
		film_türü = input("Film türünü girin: ")

		filmler[film_adı]= {"Yapım Yılı":yapım_yılı,"Imdb":imdb,"Tür":film_türü}

		print("Film başarıyla eklendi")
	else:
		print("Film adı boş bırakılamaz.")



def filmSil():
	film_adı = input("Film adı girin: ")
	if film_adı:

		filmler.pop(film_adı)
		print("Film başarıyla silindi")

	else:
		print("Film adı boş bırakılamaz.")



def filmGetir():
	aranan_film_adı= input("Aradığını filmin adını girin: ")
	if aranan_film_adı in filmler.keys():
		film = filmler.get(aranan_film_adı)
		yapım_yılı= film.get("Yapım Yılı","Yapım yılı girilmemiş")
		imdb= film.get("Imdb","Imdb puanı girilmemiş")
		film_türü= film.get("Tür","Film türü girilmemiş")

		print("Film adı: {}  Yapım Yılı: {}  Imdb: {}  Tür: {}".format(aranan_film_adı,yapım_yılı,imdb,film_türü))
	else:
		print("Film mevcut değil")
		

def filmleriListele():
	for film in filmler:
		film_adı = film
		yapım_yılı= filmler[film_adı].get("Yapım Yılı","Yapım yılı girilmemiş")
		imdb= filmler[film_adı].get("Imdb","Imdb puanı girilmemiş")
		film_türü= filmler[film_adı].get("Tür","Film türü girilmemiş")
		print("Film adı: {}  Yapım Yılı: {}  Imdb: {}  Tür: {}".format(film_adı,yapım_yılı,imdb,film_türü))
		print("="*80)
	input("Devam etmek için bir tuşa basın.")







while True:

	print("""

		[1] Tüm filmleri listele
		[2] Film ara
		[3] Film ekle
		[4] Film sil


		""")

	secenek= int(input("Seçiminizi yapın: "))
	if secenek == 1:
		filmleriListele()
	elif secenek == 2:
		filmGetir()
	elif secenek == 3:
		filmEkle()
	elif secenek == 4:
		filmSil()