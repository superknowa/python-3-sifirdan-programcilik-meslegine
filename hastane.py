#Hastane Randevu Sistemi
from datetime import date


class Hastane():
	def __init__(self,adı,adresi,bölümler,doktorlar):
		self.__adı= adı
		self.__adresi= adresi
		self.__bölümler= bölümler
		self.__doktorlar= doktorlar
		self.__rezervasyonlar= []

	def getAdı(self):
		return self.__adı

	def setAdı(self,yeni_ad):
		self.__adı= yeni_ad
		print("Hastane adı değiştirildi")

	def getAdresi(self):
		return self.__adresi

	def setAdresi(self,yeni_adres):
		self.__adresi= yeni_adres
		print("Hastane adresi değiştirildi")

	def getBölümler(self):
		print("=========Bölümlerimiz=========")
		for bölüm in self.__bölümler:
			print("""

				Bölüm: {bölüm}

				""".format(bölüm=bölüm))
			print("="*50)

	def bölümEkle(self,yeni_bölüm):
		self.__bölümler.append(yeni_bölüm)
		print("Yeni bölüm eklendi.")

	def getDoktorlar(self):
		print("=========Doktorlarımız=========")
		for doktor in self.__doktorlar:
			print("""

				İsim: {isim}
				Soyad: {soyad}
				Telefon: {telefon}
				Bölüm: {bölüm}

				""".format(isim=doktor.getİsim(),soyad=doktor.getSoyad(),telefon=doktor.getTelefon(),bölüm=doktor.getBölüm()))
			print("="*50)

	def doktorEkle(self,yeni_doktor):
		self.__doktorlar.append(yeni_doktor)
		print("Yeni doktor eklendi.")

	def rezervasyonYap(self,hasta,istenendoktor,istenentarih):
		müsaitlik= True
		for rezervasyon in self.__rezervasyonlar:
			listedeki_hasta= rezervasyon[0]
			listedeki_doktor= rezervasyon[1]
			listedeki_tarih= rezervasyon[2]

			if listedeki_doktor == istenendoktor and listedeki_tarih == istenentarih:
				print("Doktorumuz o tarihte müsait değildir.")
				müsaitlik= False
		if müsaitlik:
			self.__rezervasyonlar.append((hasta,istenendoktor,istenentarih))
			print("Rezervasyon kaydı gerçekleşti.")


	def getRezervasyonlar(self):
		print("="*50)
		print("========Rezervasyonlar========")
		rez_sayısı= 0

		for rezervasyon in self.__rezervasyonlar:
			listedeki_hasta= rezervasyon[0]
			listedeki_doktor= rezervasyon[1]
			listedeki_tarih= rezervasyon[2]

			print("{hastaismi} {hastasoyadı} isimli hastanın {rez_tarihi} tarihinde Doktor {doktorismi} {doktorsoyadı} ile randevusu vardır.".format(hastaismi=listedeki_hasta.getİsim(),hastasoyadı=listedeki_hasta.getSoyad(),rez_tarihi=listedeki_tarih,doktorismi=listedeki_doktor.getİsim(),doktorsoyadı=listedeki_doktor.getSoyad()))
			print("="*50)
			rez_sayısı+=1
		if rez_sayısı == 0:
			print("Hiçbir rezervasyon yok.")



class Birey():
	def __init__(self,isim,soyad,telefon):
		self.__isim= isim
		self.__soyad= soyad
		self.__telefon= telefon

	def getİsim(self):
		return self.__isim

	def getSoyad(self):
		return self.__soyad

	def getTelefon(self):
		return self.__telefon



class Doktor(Birey):

	doktor_sayısı= 0


	def __init__(self,isim,soyad,telefon,bölüm):
		super().__init__(isim,soyad,telefon)
		Doktor.doktor_sayısı_artır()
		self.__bölüm= bölüm

	def getBölüm(self):
		return self.__bölüm

	@classmethod
	def doktor_sayısı_artır(cls):
		cls.doktor_sayısı += 1

class Hasta(Birey):
	pass



d1= Doktor("Ali","Tosun","5425454","Kardiyoloji")
d2= Doktor("Serhat","Kabak","545455","Dahiliye")
d3= Doktor("Şenay","Sucu","54554554","Onkoloji")

h1= Hasta("Pınar","Mersinli","554555")
h2= Hasta("Halil","Kuru","5454545")

bölümler= ["KBB","Cildiye","Dahiliye","Kardiyoloji"]

hastane= Hastane("Özel Papatya","Merkez",bölümler,[d1,d2])

print("="*50)
print("{} hastanesine hoş geldiniz.".format(hastane.getAdı()))

#hastane.getBölümler()
#hastane.bölümEkle("Onkoloji")
#hastane.getBölümler()

#hastane.getDoktorlar()
#hastane.doktorEkle(d3)
#hastane.getDoktorlar()

hastane.getRezervasyonlar()

hastane.rezervasyonYap(h1,d2,date.today())
hastane.rezervasyonYap(h2,d2,date.today())


hastane.getRezervasyonlar()

print("Toplam doktor sayısı: ",Doktor.doktor_sayısı)




