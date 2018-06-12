Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> numb = []
>>> for x in range(10):
	val = input("enter no")
	numb.append(val)

enter no1
enter no2
enter no3
enter no4
enter no5
enter no6
enter no7
enter no8
enter no9
enter no10
>>> print numb
SyntaxError: Missing parentheses in call to 'print'
>>> print(numb)
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
>>> c = 0
>>> while c != 2:
	print("infinte loop")
	#c not incremented

infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loop
infinte loopTraceback (most recent call last):
  File "<pyshell#5>", line 2, in <module>
    print("infinte loop")
KeyboardInterrupt
>>> ls = []
>>> x = int(input("enter size : "))
enter size : 10
>>> for i in range(x):
	val = input("enter no")
	ls.append(i)

enter no1
enter no2
enter no3
enter no4
enter no5
enter no6
enter no7
enter no8
enter no9
enter no10
>>> ls2 = []
>>> for i in range(x):
	ls2.append(ls[i]*ls[i])

	
>>> print(ls2)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> mylist = [400,'ishita',99,'himadri',0.001,'roar']
>>> myInt = []
>>> myFlt = []
>>> myStr = []
>>> for x in mylist:
	if isinstance(x,int):
		myInt.append(x)
	if isinstance(x,str):
		myStr.append(x)
	if isinstance(x,float):
		myFlt.append(x)

>>> print(myInt)
[400, 99]
>>> print(myFlt)
[0.001]
>>> ptint(myStr)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    ptint(myStr)
NameError: name 'ptint' is not defined
>>> print(myStr)
['ishita', 'himadri', 'roar']
>>> meEven = []
>>> meOdd = []
>>> for x in range(1,101):
       if x%2 == 0:
	       meEven.append(x)
       else:
	       meOdd.append(x)

	       
>>> print(meEven)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> print(meOdd)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> for i in range(0,4):
	for j in range(0,i+1):
		print("*")
	print("\n")

	
*


*
*


*
*
*


*
*
*
*


>>> i = len(dic.items())
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    i = len(dic.items())
NameError: name 'dic' is not defined
>>> dic = {}
>>> for i in range(3):
	key = input()
	value = int(input())
	dic[key] = value

	
a
1
b
2
c
3
>>> i = len(dic.items())
>>> c = 0
>>> while c < i:
	k,v =list(dic.items())[c]
	print(k,v)
	c+=1

	
a 1
b 2
c 3
>>> num = []
>>> x = int(input("enter size : "))
enter size : 5
>>> for i in range(x):
	val = input("enter no")
	num.append(i)

	
enter no1
enter no2
enter no3
enter no4
enter no5
>>> rem = int(input("enter number to be removed: "))
enter number to be removed: 4
>>> num.remove(rem)
>>> print(rem)
4
>>> 
