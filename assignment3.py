Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 'Himadri','Ishita',100,True
>>> type(x)
<class 'tuple'>
>>> len(x)
4
>>> y = 1,2,3,4,0
>>> type(y)
<class 'tuple'>
>>> min(y)
0
>>> max(y)
4
>>> tup=(1,4,6,9,10,12)
>>> product=(1*4*6*9*10*12)
>>> print(product)
25920
>>> a = input("enter values in set 1")
enter values in set 11,2,3,4,5
>>> type(a)
<class 'str'>
>>> a = set(a)
>>> b = input("enter value of set 2: ")
enter value of set 2: 6,7,8,9,10
>>> b = set(b)
>>> a - b
{'2', '4', '5', '3'}
>>> a.difference(b)
{'2', '4', '5', '3'}
>>> a == b
False
>>> a & b
{',', '1'}
>>> dic = {}
>>> for i in range(10):
	key = input()
	value = int(input())
	dic[key] = value

	
1
1
2
2
3
3
4
4
5
5
6
6
7
7
8
8
9
9
10
10
>>> dic
{'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10}
>>> 
