#4-dasturimiz "Sonlarni solishtirib ular ustida amal bajarish masalasi"
son1= int(input("1-sonni kiriting: "))
son2= int(input("2-sonni kiriting: "))


min = (son1+ son2)/2
max =2* son1* son2
if son1  > son2:
   son1,son2 = max, min
elif son1< son2:
	son1,son2 =min, max

print(f"{son1}  {son2}")
"""
kutilgan natija :
	
	1-sonni kiriting: 7
2-sonni kiriting: 2
28  4.5

[Program finished]
"""
