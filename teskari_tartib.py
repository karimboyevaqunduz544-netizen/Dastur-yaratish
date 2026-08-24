#Pythonda kiritilgan sonni teskari tartibda chiqarish
son = int(input("Uch xonali son kiriting:"))
x = son // 100 #yuzliklar xonasi
y = son // 10%10 #o'nliklar xonasu
z = son % 10 #birliklar xonasi
print(f"Siz kiritgan son teskari tartibda {z}{y}{x}")
"""
  Output:
Uch xonali son kiriting:732
Siz kiritgan son teskari tartibda 237
"""
