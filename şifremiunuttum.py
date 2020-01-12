#====Unutulmuş Şifreyi Mail Gönderen Uygulama======
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def şifreyi_getir(kullanıcı_adı):
	dosya= open("kullanıcılar.txt","r")
	satırlar= dosya.readlines()

	for kullanıcı in satırlar:
		bölünmüş= kullanıcı.split()
		k_adı= bölünmüş[0]
		şifre= bölünmüş[1]
		mail= bölünmüş[2]
		if kullanıcı_adı == k_adı:
			şifreyi_mail_gönder(kullanıcı_adı=kullanıcı_adı,mail=mail,şifre=şifre)


def şifreyi_mail_gönder(kullanıcı_adı,mail,şifre):

	gönderici_maili= "testerjoe1111@gmail.com"
	mesaj_içeriği= """

			Merhabalar {kullanıcı_adı};
			Şifrenizi unutmuşsunuz ve {tarih} tarihinde mailinize gönderilmesini talep ettiniz.

			Şifreniz: {şifre}


	"""

	mesaj= MIMEMultipart()
	mesaj["Subject"]= "Şifreniz Gönderildi"
	mesaj["From"]= gönderici_maili
	mesaj["To"]= mail

	tarih_bugün= datetime.now()

	mesaj_formatlanmış= mesaj_içeriği.format(kullanıcı_adı=kullanıcı_adı,tarih=tarih_bugün.strftime("%d/%m/%Y %H:%M:%S"),şifre=şifre)

	mesaj.attach(MIMEText(mesaj_formatlanmış,"plain"))


	mail_servisi= smtplib.SMTP("smtp.gmail.com",587)
	mail_servisi.ehlo()
	mail_servisi.starttls()
	mail_servisi.login("testerjoe1111@gmail.com","deneme1234")
	mail_servisi.sendmail(gönderici_maili,mail,mesaj.as_string())
	mail_servisi.quit()
	print("Mailiniz gönderildi.")



if __name__ == "__main__":
	şifreyi_getir("pythoncı")