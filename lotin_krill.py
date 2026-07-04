#Lotin harflarni krelchaga ozgartiuvchi dastur yaratamiz
soz = input("So'z kiriting: ")
ozgartirilgan_soz = " "
lugat = {
    'a': 'a', 'b': 'б', 'd': 'д', 'e': 'е', 'f': 'ф', 'g': 'г',
    'h': 'ҳ', 'i': 'и', 'j': 'ж', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п',
    'q': 'қ', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у',
    'v': 'в', 'x': 'х', 'y': 'й', 'z': 'з', 'o`': 'ў', 'g`': 'ғ',
    'sh': 'ш', 'ch': 'ч'}
for i in range(len(soz)):
    if i + 1 < len(soz) and soz[i] == "s" and soz[i+1] == "h":
        ozgartirilgan_soz += lugat[soz[i] + soz[i+1]]
    elif i > 0 and soz[i] == "h" and soz[i-1] == "s":
        continue
    elif i + 1 < len(soz) and soz[i] == "c" and soz[i+1] == "h":
        ozgartirilgan_soz += lugat[soz[i] + soz[i+1]]
    elif i > 0 and soz[i] == "h" and soz[i-1] == "c":
        continue
    elif soz[i] in lugat.keys():
        ozgartirilgan_soz += lugat[soz[i]]
    elif soz[i] in lugat.values():
        for a, b in lugat.items():
            if soz[i] == b:
                ozgartirilgan_soz += a
    else:
        ozgartirilgan_soz += soz[i]

print(ozgartirilgan_soz)
"""
Konsoldagi ishga tushish natijasi (Example output):
-------------------------------------------------
So'z kiriting: shahar, anor, choy
Natija: шаҳар, анор, чой
-------------------------------------------------
"""
