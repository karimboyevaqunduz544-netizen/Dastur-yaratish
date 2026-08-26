
"""
N natural son berilgan Shu songacha bolgan mukammal sonlarni chiqaruvchi programma tuzilsin.O'zidan boshqa bo'luvchilari  yigindisi  o'ziga teng bolgan son mukammal son deyiladi. Masalan: 6;28(Kiruvchi ma'lumotlar: 100 : 6; 28
  10000 : 6; 28; 496;8128)
"""
#! 6-> 1 2 3
#! 28 -> 1 2 4 7 14
N = int(input(" N kiriting :"))
perfect_numbers = []

def find_sum_of_devisor(num):
	total = 0
	
	for i in range(1, num):
		if num % i == 0:
			total += i
	return total
for number in range(2, N + 1):
    if     number==find_sum_of_devisor(number):
    	perfect_numbers.append(number)
print(perfect_numbers)
N = int(input("N kiriting: "))
perfect_numbers = []

def find_sum_of_devisor(num):
    if num <= 1:
        return 0
    total = 1
    # Sonning ildizigacha bo'lgan bo'luvchilarni tekshirish
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            total += i
            if i != num // i:
                total += num // i
    return total

for number in range(2, N + 1):
    if number == find_sum_of_devisor(number):
        perfect_numbers.append(number)

print("Mukammal sonlar:", perfect_numbers)

"""
N kiriting :100
[6, 28]
N kiriting: 10000
Mukammal sonlar: [6, 28, 496, 8128]

"""
