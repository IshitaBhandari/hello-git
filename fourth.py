Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> year = int(input("enter year"))
enter year2004
>>> if (year % 4) == 0:
	if (year % 100) == 0:
		if(year % 400) == 0:
			print("leap year")
		else:
			print("not a leap year")
	else:
		print("leap year")
else:
	print("not a leap year")

leap year
>>> length = int(input("enter length"))
enter length10
>>> breadth = int(input("enter breadth"))
enter breadth10
>>> if length == breadth:
	print("dimensions of square" )
else:
	print("dimensions of rectangle")

	
dimensions of square
>>> first = int(input("enter the first person's age "))
enter the first person's age 12
>>> second = int(input("enter the second person's age "))
enter the second person's age 19
>>> third = int(input("enter the third person's age "))
enter the third person's age 8
>>> if first >= second and first >= third:
	print("first is oldest")
elif second >= first and second >= third:
	print("second is oldest")
elif third >= first and third >= second:
	print("third is oldest")

second is oldest
>>> 
if first <= second and first <= third:
	print("first is youngest")
elif second <= first and second <= third:
	print("second is youngest")
elif third <= first and third <= second:
	print("third is youngest")

	
third is youngest
>>> points = int(input("enter the points:"))
enter the points:160
>>> if points > 0 and points <= 200:
	if points <= 50:
		print("sorry!no prize this time")
	elif points >= 51 and points <= 151:
		print("congratulations! you won a wooden dog")
	elif points >= 151 and points <= 180:
		print("congratulations! you won a book")
	elif points >= 181 and points <= 200:
		print("congratulations! you won chocolates")
else:
	print("invalid input")

congratulations! you won a book
>>> quantity = int(input("enter the quantity"))
enter the quantity20
>>> cost=100*quantity
>>> if cost > 1000:
	print((cost*90/100))
else:
	print(cost)

	
1800.0
>>> 
