Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def area(rad):
	ar = 3.14*rad*rad
	print(ar)

>>> rad = int(input("enter no.:"))
enter no.:2
>>> area(rad)
12.56
>>> def per():
	sum = 0
	i = 1
	while sum < 1000:
		sum+=i
		print(sum)
		i+=1

		
>>> per()
1
3
6
10
15
21
28
36
45
55
66
78
91
105
120
136
153
171
190
210
231
253
276
300
325
351
378
406
435
465
496
528
561
595
630
666
703
741
780
820
861
903
946
990
1035
>>> def mul(n,i):
	if i <= 10:
		print(str(n)+"*"+str(i)+"="+str(n*i))
		#recursively calling mul 
		mul(n,i+1)
		
	else:
		#to stop recursion fn
		print()

>>> mul(12,1)
12*1=12
12*2=24
12*3=36
12*4=48
12*5=60
12*6=72
12*7=84
12*8=96
12*9=108
12*10=120

>>> def poww(a,b,i,prod):
	if(i <= b):
		prod = prod * a
		poww(a,b,i+1,prod)
	else:
		print(prod)

		
>>> poww(2,3,1,1)
8
>>> def facto(n):
	s = 0
	#n+1 to go from 1 to 5 completely
	for i in range(1,n+1):
		s *= i
	#store in dictionary	
	dic[n]=s

>>> facto(5)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    facto(5)
  File "<pyshell#11>", line 7, in facto
    dic[n]=s
NameError: name 'dic' is not defined
>>> dic = {}
>>> def facto(n):
	s = 1
	#n+1 to go from 1 to 5 completely
	for i in range(1,n+1):
		s *= i
	#store in dictionary	
	dic[n]=s

	
>>> facto(5)
>>> print(dic)
{5: 120}
>>> 
