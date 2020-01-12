#Property İle Salt Okunur Nitelik Oluşturma  |  Değiştirme   | Silme

class Kitap():
	def __init__(self,başlık):
		self.__başlık = başlık

	@property
	def başlık(self):
		return self.__başlık

	@başlık.setter
	def başlık(self,yeni_başlık):
		self.__başlık= yeni_başlık
		print("Başlık güncellendi")

	@başlık.deleter
	def başlık(self):
		del self.__başlık
		print("__başlık niteliği silindi")



k1= Kitap("Sefiller")

del k1.başlık
