#E-Posta Servisi Uygulaması

from datetime import datetime
import os,time



class EPostaServisi():
	def __init__(self,isim):
		self.__isim= isim
		self.__üyeler= [("Tarık","Demir","şakşuka@ultramail.com","abc123")]
		self.__gönderilmiş_mailler= []

	def __str__(self):
		return self.__isim + " servisine hoş geldiniz."


	def üyeOl(self,isim,soyad,mail,şifre):
		if self.kontrol(mail):
			print("Mail serbest")
			yeni_üye= isim,soyad,mail,şifre
			self.__üyeler.append(yeni_üye)
			print("Kayıt gerçekleşti")
			input("Devam etmek için bir tuşa basın.")
		else:
			print("Bu mail zaten alınmış")
			input("Başka bir mail denemek için bir tuşa basın.")

	def girişYap(self,mail,şifre):
		if self.şifreKontrol(mail,şifre):
			print("Giriş Yapıldı")
			time.sleep(1)
			print("Kullanıcı menüsüne yönlendiriliyorsunuz...")
			time.sleep(1)
			self.kullanıcıMenüsü(mail)

		else:
			print("Mail veya şifre hatalı!")
			time.sleep(1)

	def kullanıcıMenüsü(self,mail):
		while True:
			os.system(temizle)
			print("""

				[1] Mail Gönder [2] Mail Kutusuna Git [3] Çıkış Yap

				""")
			seçim= int(input("Seçiminizi girin: "))

			if seçim == 1:
				self.mailGönder(mail)
			elif seçim == 2:
				self.mailKutusu(mail)
			elif seçim == 3:
				break

	def mailGönder(self,mail):
		alıcı= input("Alıcının mail adresini girin: ")
		başlık= input("Mail başlığını girin: ")
		mesaj= input("Mesajınızı yazın: ")
		yeni_mail= Mail(mail,alıcı,başlık,mesaj)
		self.__gönderilmiş_mailler.append(yeni_mail)
		print("Mail gönderildi")
		time.sleep(1)
		print("Sizi ana menüye yönlendiriyorum")
		time.sleep(1)

	def mailKutusu(self,mail):
		mail_var= False
		for m in self.__gönderilmiş_mailler:
			if m.getGönderici() == mail or m.getAlıcı() == mail:
				mail_var= True
				print(m)
		if not mail_var:
			print("Mail kutunuz boş")
		input("Devam etmek için bir tuşa basın.")


	def şifreKontrol(self,mail,şifre):
		for üye in self.__üyeler:
			kayıtlı_mail= üye[2]
			kayıtlı_şifre= üye[3]
			if kayıtlı_mail == mail and kayıtlı_şifre == şifre:
				return True
		return False


	def kontrol(self,mail):
		for üye in self.__üyeler:
			kayıtlı_mail= üye[2]
			if kayıtlı_mail == mail:
				return False
		return True



class Mail():
	def __init__(self,kimden,kime,başlık,mesaj):
		self.__kimden= kimden
		self.__kime= kime
		self.__başlık= başlık
		self.__mesaj= mesaj
		self.__tarih= datetime.now().strftime("%d/%m/%Y %H:%M:%S")

	def getGönderici(self):
		return self.__kimden

	def getAlıcı(self):
		return self.__kime

	def __str__(self):
		return """

		==============================================================
				
		Gönderici: {gönderici}   Alıcı: {alıcı} Tarih: {tarih}

		==============================================================

		Başlık: {konu_başlığı}

		==============================================================

		Mesaj: {mesaj}

		==============================================================

		""".format(gönderici=self.__kimden,alıcı= self.__kime,tarih=self.__tarih,konu_başlığı=self.__başlık,mesaj=self.__mesaj)



temizle= ("cls" if os.name=="nt" else "clear")
e1= EPostaServisi("Ultra Mail X")

#e1.üyeOl("Selçuk","Apar","tosbik@ultramailx.com","abc123")


menü= """

		{başlık}
		[1] Yeni Mail Adresi Al
		[2] Giriş Yap
		[3] Çıkış


""".format(başlık=e1)


while True:
	try:
		os.system(temizle)
		print(menü)
		seçim= int(input("Seçiminizi girin: "))

		if seçim == 1:

			isim= input("İsim: ")
			soyad= input("Soyad: ")
			mail= input("Mail adresi: ")
			şifre= input("Şifre: ")

			if isim and soyad and mail and şifre:
				e1.üyeOl(isim,soyad,mail,şifre)
			else:
				print("Tüm bilgileri girmeniz gerekir!")
		elif seçim == 2:
			e1.girişYap(mail=input("Mailinizi girin: "),şifre=input("Şifrenizi girin: "))

		elif seçim == 3:
			quit()
		else:
			raise ValueError("Girdiğiniz sayılar sadece 1,2 ve 3 olabilir")
	except ValueError as mesaj:
		print("Geçersiz bir değer girdiniz: " + str(mesaj))
		time.sleep(1)


