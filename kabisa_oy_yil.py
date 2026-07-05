#1-mashq Kabisa oyi (yili)ni topuvchi dastur
"""
Kiruvchi ma'lumotlar : shularni sinab koramiz(Oy va yil)
	 2 ;2020
     2; 1900
     8; 2026
"""
oy = int(input("1- Oy raqamini kiriting (1-12): "))
yil = int(input(" 1- Yilni kiriting: "))

if oy in [1, 3, 5, 7, 8, 10, 12]:
    kun = 31
elif oy in [4, 6, 9, 11]:
    kun = 30
elif oy == 2:
    
    if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
        kun = 29
    else:
        kun = 28
else:
    kun = "Xato oy raqami!"

print(f"Natija: {kun}")
oy = int(input("2-Oy raqamini kiriting (1-12): "))
yil = int(input("2- Yilni kiriting: "))

if oy in [1, 3, 5, 7, 8, 10, 12]:
    kun = 31
elif oy in [4, 6, 9, 11]:
    kun = 30
elif oy == 2:
    
    if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
        kun = 29
    else:
        kun = 28
else:
    kun = "Xato oy raqami!"

print(f"Natija: {kun}")
oy = int(input("3 - Oy raqamini kiriting (1-12): "))
yil = int(input(" 3-Yilni kiriting: "))

if oy in [1, 3, 5, 7, 8, 10, 12]:
    kun = 31
elif oy in [4, 6, 9, 11]:
    kun = 30
elif oy == 2:
    
    if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
        kun = 29
    else:
        kun = 28
else:
    kun = "Xato oy raqami!"

print(f"Natija: {kun}")

#Kabisa  deb 4ga karralilarga aytiladi.Lekin 100 ga karralilar  ichida faqat 400 ga karrali bolganlari kabisa hisoblanadi

"""
Natija quyidagicha:

1- Oy raqamini kiriting (1-12): 2
 1- Yilni kiriting: 2020
Natija: 29
2-Oy raqamini kiriting (1-12): 2
2- Yilni kiriting: 1900
Natija: 28
3 - Oy raqamini kiriting (1-12): 8
 3-Yilni kiriting: 2026
Natija: 31

[Program finished]
"""
