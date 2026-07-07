#Masala.If_Asr turi(Yilga qadab Asrni va uninv turini aniqlash)
"""
Masala sharti:
	Musbat  butun son  korinishida yil berilgan.(Masalan, 2026)Ushbu yil nechançhi asrga togri kelishi va u "Yangi asr boshlanish yili"(Centinnial year, ya'ni 100 ga qoldiqsiz bolinadigan yil masalan:1900, 2000) yoki oddiy yil ekanini aniqlovchi dastur tuzing.
Kiruvchi malumotlar:    Natija:
2026                        21-asr , oddiy yil
2000                        20-asr, yangi asr  boshlanish yil
1801                        19-asr, oddiy yil
        Maslahat! Asrni topish uchun formula:
 Asr = (Yil-1)//100+1. Yangi asr boshlanish yili ekanligini :
 Yil%100==0 orqali aniqlang
 """
yil = int(input("1- Yilni kiriting: "))
asr = (yil-1)//100+1
if yil %100 == 0:
 yil_turi = "Yangi asr boshlanish yili"
else:
 yil_turi = "oddiy yil"
 
 # 3. Natijani f-string yordamida chiroyli chiqarish
print(f"Natija: {asr}-asr, {yil_turi}")

yil = int(input("2- Yilni kiriting: "))
asr = (yil-1)//100+1
if yil %100 == 0:
 yil_turi = "Yangi asr boshlanish yili"
else:
 yil_turi = "oddiy yil"
 
 
print(f"Natija: {asr}-asr, {yil_turi}")
 
yil = int(input("3- Yilni kiriting: "))
asr = (yil-1)//100+1
if yil %100 == 0:
 yil_turi = "Yangi asr boshlanish yili"
else:
 yil_turi = "oddiy yil"
print(f"Natija: {asr}-asr, {yil_turi}")

"""
kutilgan natija:
 1- Yilni kiriting: 2026
Natija: 21-asr, oddiy yil
2- Yilni kiriting: 2000
Natija: 20-asr, Yangi asr boshlanish yili
3- Yilni kiriting: 1801
Natija: 19-asr, oddiy yil

[Program finished]
