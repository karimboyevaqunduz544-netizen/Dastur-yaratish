#Masala. If_vaxt_Asr(Chorak va fasllar mantiqi)

"""
Foydalanuvchi oy raqamini kiritadi(1 dan 12 gacha).Dastur ushbu oy qaysi faslga (Qish, bahor, yoz , kuz) va yilning qaysi choragiga (1-chorak: 1-3- oylar,2- chorak: 4-6oylar  va hk)tegishli ekanini chop etish kerak. Agar oy raqami notogri bolsa, "Xato oy raqami " deb chiqsin 
Berilgan malumotlar : 12 ; 5 ; 15.(oy raqami)

Natija:  Qish fasli 4-chorak ; Bahor fasli 2-chorak ; Xato oy raqami

"""

#boshladik


oy = int(input("1- oy raqamini kiriting (1-12): "))

# Avval kiritilgan oy raqami to'g'ri ekanligini tekshiramiz
if oy < 1 or oy > 12:
    print("Xato oy raqami")
else:
    # Fasllarni aniqlash mantiqi
    if oy == 12 or oy == 1 or oy == 2:
        fasl = "Qish fasli"
    elif oy == 3 or oy == 4 or oy == 5:
        fasl = "Bahor fasli"
    elif oy == 6 or oy == 7 or oy == 8:
        fasl = "Yoz fasli"
    else:
        fasl = "Kuz fasli"

    # Choraklarni aniqlash mantiqi
    if 1 <= oy <= 3:
        chorak = "1-chorak"
    elif 4 <= oy <= 6:
        chorak = "2-chorak"
    elif 7 <= oy <= 9:
        chorak = "3-chorak"
    else:
        chorak = "4-chorak"

    # Natijani ekranga chiqarish
    print(f"Natija: {fasl}, {chorak}")

oy = int(input("2-y raqamini kiriting (1-12): "))

# Avval kiritilgan oy raqami to'g'ri ekanligini tekshiramiz
if oy < 1 or oy > 12:
    print("Xato oy raqami")
else:
    # Fasllarni aniqlash mantiqi
    if oy == 12 or oy == 1 or oy == 2:
        fasl = "Qish fasli"
    elif oy == 3 or oy == 4 or oy == 5:
        fasl = "Bahor fasli"
    elif oy == 6 or oy == 7 or oy == 8:
        fasl = "Yoz fasli"
    else:
        fasl = "Kuz fasli"

    # Choraklarni aniqlash mantiqi
    if 1 <= oy <= 3:
        chorak = "1-chorak"
    elif 4 <= oy <= 6:
        chorak = "2-chorak"
    elif 7 <= oy <= 9:
        chorak = "3-chorak"
    else:
        chorak = "4-chorak"

    # Natijani ekranga chiqarish
    print(f"Natija: {fasl}, {chorak}")

oy = int(input("3-oy raqamini kiriting (1-12): "))

# Avval kiritilgan oy raqami to'g'ri ekanligini tekshiramiz
if oy < 1 or oy > 12:
    print("Xato oy raqami")
else:
    # Fasllarni aniqlash mantiqi
    if oy == 12 or oy == 1 or oy == 2:
        fasl = "Qish fasli"
    elif oy == 3 or oy == 4 or oy == 5:
        fasl = "Bahor fasli"
    elif oy == 6 or oy == 7 or oy == 8:
        fasl = "Yoz fasli"
    else:
        fasl = "Kuz fasli"

    # Choraklarni aniqlash mantiqi
    if 1 <= oy <= 3:
        chorak = "1-chorak"
    elif 4 <= oy <= 6:
        chorak = "2-chorak"
    elif 7 <= oy <= 9:
        chorak = "3-chorak"
    else:
        chorak = "4-chorak"

    # Natijani ekranga chiqarish
    print(f"Natija: {fasl}, {chorak}")
    """
    chiqgan natija quyidagicha
    

1- oy raqamini kiriting (1-12): 12
Natija: Qish fasli, 4-chorak
2-y raqamini kiriting (1-12): 5
Natija: Bahor fasli, 2-chorak
3-oy raqamini kiriting (1-12): 15
Xato oy raqami

"""
