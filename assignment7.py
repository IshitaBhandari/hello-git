Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Write a program to get formatted time
>>> import time
>>> import math
>>> import os
>>> print(time.strftime("%H:%M:%S"))
15:54:10
>>> #Extract month from the time
>>> '''The function strftime takes '2' arguments one format and another time strftime(format,t = time)
'''
"The function strftime takes '2' arguments one format and another time strftime(format,t = time)\n"
SyntaxError: multiple statements found while compiling a single statement
>>> '''The function strftime takes '2' arguments one format and another time strftime(format,t = time)
'''
"The function strftime takes '2' arguments one format and another time strftime(format,t = time)\n"
>>> print(time.strftime("%B,%m"))
June,06
>>> # Extract day from the time
>>> print(time.strftime("%d, %j"))
14, 165
>>> #Extract date (ex : 11 in 11/01/2021) from the time
>>> print(time.strftime("%d in %d/%m/%Y"))
14 in 14/06/2018
>>> #Write a program to print time using localtime method
>>> localtime = time.localtime(time.time())
>>> print("Local current time :", localtime)
Local current time : time.struct_time(tm_year=2018, tm_mon=6, tm_mday=14, tm_hour=15, tm_min=57, tm_sec=11, tm_wday=3, tm_yday=165, tm_isdst=0)
>>> #Find the factorial of a number input by user using math package functions
>>> no=int(input('enter a no:'))
enter a no:5
>>> print(math.factorial(no))
120
>>> #Find the GCD of a number input by user using math package functions
>>> a=int(input('enter 1st no:'))
enter 1st no:30
>>> b=int(input('enter 2nd no:'))
enter 2nd no:45
>>> print(math.gcd(a,b))
15
>>> #Use OS package and do the following tasks:  Get current working directory.Get the user environment
>>> print(os.getcwd())
C:\Users\HP\AppData\Local\Programs\Python\Python36-32
>>> print(os.getenv('TEMP'))
C:\Users\HP\AppData\Local\Temp
>>> 
