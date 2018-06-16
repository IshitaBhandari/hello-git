Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Animal():
	legs = 4
	ears = 2
	tail = 1
	
	def animal_attribute(self):
		print("This animal has %d legs"%self.legs)
		print("This animal has %d ears"%self.ears)
		print("This animal has %d tail"%self.tail)

		
>>> #This class inherits legs, ears & tail arguments from Animal class
>>> #This class has it's argument typ that tells what type of food preference does it have
>>> class Tiger(Animal):
	typ = "carnivorous"
	#we will access the base class method through a function
	def access(self):
		print("This animal is %d  "%self.typ)
		print("This animal has %d legs"%self.legs)
		print("This animal has %d ears"%self.ears)
		print("This animal has %d tail"%self.tail)

		
>>> obj = Animal()
>>> obj.animal_attribute()
This animal has 4 legs
This animal has 2 ears
This animal has 1 tail
>>> obj1 = Tiger()
>>> obj1.animal_attribute()
This animal has 4 legs
This animal has 2 ears
This animal has 1 tail
>>> class A():
	def f(self):
		return self.g()
	def g(self):
		return 'A'

>>> class B(A):
	def g(self):
		return 'B'

	
>>> a = A()
>>> b = B()
>>> #The g() method of that class will be called who's object has created to call with.
>>> #Here a object is of class A(). Therefore, a.f() will call class A's method - g().
>>> #And, b object is of class B(). Therefore, b.f() will call class B's method - g().
>>> print
<built-in function print>
>>> print(a.f(),b.f())
A B
>>> class Cop():
	def __init__(self,name,age,workexp,desig):
		self.name = name
		self.age = age
		self.workexp = workexp
		self.desig = desig
	def display(self):
		print(self.name+"\n"+self.age+"\n"+self.workexp+"\n"+self.desig)
	def update(self):
		self.name = input("enter new name")
		self.age = input("enter new age")
		self.workexp = input("enter new work experience")
		self.desig = input("enter new designation")

>>> class Mission(Cop):
	def add_mission_details(self,country,file):
		self.country = country
		self.file = file

		
>>> 
KeyboardInterrupt
>>> cobj = Cop(input("name?:"),input("age?:"),input("work experience"),input("designation?:"))
name?:mike
age?:35
work experience8
designation?:ninja
>>> mobj = Mission(input("name?:"),input("age?:"),input("work experience"),input("designation?:"))
name?:josh
age?:20
work experience1
designation?:agent
>>>  mobj.add_mission_details("aus","V")
 
SyntaxError: unexpected indent
>>> 
KeyboardInterrupt
>>> mobj.add_mission_details("aus","V")
>>> mobj.display()
josh
20
1
agent
>>> class Shape():
	def __init__(self,length,breadth):
		self.length = length
		self.breadth = breadth
	def Area(self):
		return(self.breadth * self.length)

>>> class Rectangle(Shape):
	def display(self):
		print(self.Area())

		
>>> class Square(Shape):
	def display_s(self):
		print(self.Area())

		
>>> robj = Rectangle(10,4)
>>> robj.display()
40
>>> sobj = Square(2,2)
>>> sobj.display()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    sobj.display()
AttributeError: 'Square' object has no attribute 'display'
>>> 
