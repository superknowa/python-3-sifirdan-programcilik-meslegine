harfler= "abcdefgğhıijklmnoöprsştuüvyz"

kelime= "Hey"
kelime= kelime.lower()


şifreli_kelime= harfler[harfler.index(kelime[0]) + 1] + harfler[harfler.index(kelime[1]) + 1] + harfler[harfler.index(kelime[2]) + 1]


print(kelime[0] + "------>" + harfler[harfler.index(kelime[0])+1])
print(kelime[1] + "------>" + harfler[harfler.index(kelime[1])+1])
print(kelime[2] + "------>" + harfler[harfler.index(kelime[2])+1])


print(kelime," kelimesinin şifreli hali:", şifreli_kelime)






şifresi_kırılmış_hali= harfler[harfler.index(şifreli_kelime[0]) - 1] + harfler[harfler.index(şifreli_kelime[1]) - 1] + harfler[harfler.index(şifreli_kelime[2]) - 1]

print(şifreli_kelime[0] + "------>" + harfler[harfler.index(şifreli_kelime[0])-1])
print(şifreli_kelime[1] + "------>" + harfler[harfler.index(şifreli_kelime[1])-1])
print(şifreli_kelime[2] + "------>" + harfler[harfler.index(şifreli_kelime[2])-1])



print(şifreli_kelime," kelimesinin şifresi çözülmüş hali:", şifresi_kırılmış_hali)