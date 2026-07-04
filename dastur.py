
#Sonlarni eng kichigini aniqlovchi dastur yaratamiz
a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: " ))
c = int(input("3-sonni kiriting: "))

if a<b and a<c:
	print(a)
elif c<a and c<b:
	print(c)
elif b<a and b<c:
	print(b)
else:
		print("Bunday son mavjud emas")
	
