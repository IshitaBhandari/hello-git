Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import threading
>>> import time
>>> class myThread(threading.Thread):
	def __init__(self,name):
		threading.Thread.__init__(self)
		self.name=name
	def run(self):
		print("starting: " + self.name)
		time.sleep(5)
		print("hi")
		print("exiting:" + self.name)

		
>>> obj = myThread(1)
>>> obj.setName('ishita')
>>> obj.start()
starting: ishita
>>> 
hi
exiting:ishita

>>> 
KeyboardInterrupt
>>> class myThreadTwo(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def count(self):
		print("starting count:")
		for i in range(1,10):
			print(i)
			time.sleep(1)
		print("stopping")

		
>>> obj = myThreadTwo()
>>> obj.count()
starting count:
1
2
3
4
5
6
7
8
9
stopping
>>> class MyThreadThree(threading.Thread):
	def __init__(self,lis,name):
		threading.Thread.__init__(self)
		self.lis = lis
		self.name = name
	def run(self):
		print("starting:" + self.name)
		for i in range(0,5):
			time.sleep(i * 2)
			print(lis[i])
		print("exiting" + self.name)

		
>>> lis = [2,3,4,5,6]
>>> obj = MyThreadThree(lis,"ishita")
>>> obj.run()
starting:ishita
2
3
4
5
6
exitingishita
>>> import math
>>> def fact():
	num=int(input("enter number"))
	res = math.factorial(num)
	print("factorial:",res)

	
>>> obj.Thread(target=fact).start()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    obj.Thread(target=fact).start()
AttributeError: 'MyThreadThree' object has no attribute 'Thread'
>>> threading.Thread(target=fact).start()
enter number5
>>> factorial: 120
