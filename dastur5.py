"""
5! Berilgan sanadan keyingi sanani topib beruvchi dastur yaratish

Ikkita butun son berilgan Day(kun) va Month(oy)
(Kabisa bolmagam yil sanasi kiritiladi).(sinab koring quyidagilarni: 19;3 , 9; 9 ,  32; 6"))
"""

oy_kunlari = [31,28,31,30,31,30,31,31,30,31,30,31]
oy = int(input("1- Oyni kiriting: "))
kun= int(input("1- Kunni kiriting: "))

if oy < 1 or oy > 12:
   print("Bunday oy yoq")
elif kun < 1 or kun > oy_kunlari[oy-1 ] :
   print("Bunday kun yoq")
else:
       if kun == oy_kunlari [oy-1]:
           oy  += 1
           kun = 1
       else:
           kun += 1

if oy > 12:
        oy = 1  # Yangi yil boshlanishi uchun oy professional kodda 1 ga qaytariladi

print(f"Ertangi sana: {kun}-{oy}")
	
oy_kunlari = [31,28,31,30,31,30,31,31,30,31,30,31]
oy = int(input("2-Oyni kiriting: "))
kun= int(input("2-Kunni kiriting: "))

if oy < 1 or oy > 12:
   print("Bunday oy yoq")
elif kun < 1 or kun > oy_kunlari[oy-1 ] :
   print("Bunday kun yoq")
else:
       if kun == oy_kunlari [oy-1]:
           oy  += 1
           kun = 1
       else:
           kun += 1

if oy > 12:
        oy = 1  # Yangi yil boshlanishi uchun oy professional kodda 1 ga qaytariladi

print(f"Ertangi sana: {kun}-{oy}")


oy_kunlari = [31,28,31,30,31,30,31,31,30,31,30,31]
oy = int(input("3-Oyni kiriting: "))
kun= int(input("3-Kunni kiriting: "))

if oy < 1 or oy > 12:
   print("Bunday oy yoq")
elif kun < 1 or kun > oy_kunlari[oy-1 ] :
   print("Bunday kun yoq")
else:
       if kun == oy_kunlari [oy-1]:
           oy  += 1
           kun = 1
       else:
           kun += 1

if oy > 12:
        oy = 1  # Yangi yil boshlanishi uchun oy professional kodda 1 ga qaytariladi

print(f"Ertangi sana: {kun}-{oy}")

"""
kutilgan natija:
	1- Oyni kiriting: 19
1- Kunni kiriting: 3
Bunday oy yoq
Ertangi sana: 3-1
2-Oyni kiriting: 9
2-Kunni kiriting: 9
Ertangi sana: 10-9
3-Oyni kiriting: 32
3-Kunni kiriting: 6
Bunday oy yoq
Ertangi sana: 6-1

[Program finished]
"""
