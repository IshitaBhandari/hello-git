Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #print something
>>> print("How was your day?")
How was your day?
>>> print("Acad" + "View")
AcadView
>>> x = input("enter x:")
enter x:10
>>> y = input("enter y:")
enter y:20
>>> z = input("enter z:")
enter z:30
>>> print(x,y,z)
10 20 30
>>> print("Let's get started")
Let's get started
>>> s = "Acadview"
>>> course = "Python"
>>> fees = 5000
>>> print('%s %s %d' (s,course,fees))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print('%s %s %d' (s,course,fees))
TypeError: 'str' object is not callable
>>> print('%s %s %d' % (s,course,fees))
Acadview Python 5000
>>> name="Tony Stark"
>>> salary = 1000000
>>> print('%s' '%d')%(name,salary)
%s%d
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print('%s' '%d')%(name,salary)
TypeError: unsupported operand type(s) for %: 'NoneType' and 'tuple'
>>> print(('%s' '%d')%(name,salary))
Tony Stark1000000
>>> 
