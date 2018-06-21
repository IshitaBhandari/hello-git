Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> try:
    a = 3
    if a < 4:
        a = a / (a - 3)
except (ZeroDivisionError, IndentationError):
    print("The answer is 0.")
else:
    print(a)

    
The answer is 0.
>>> #answer 1: The error that has occurred is IndentationError : unexpected indent and also ZeroDivisionError : division by zero
>>> try:
    l = [1, 2, 3]
    print(l[3])
except IndexError:
    print("Cannot access this Element.")

Cannot access this Element.
>>> #answer 2:IndexError: list index out of range
>>> """try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print
    "An exception"
    raise  # To determine whether the exception was raised or not"""
'try:\n    raise NameError("Hi there")  # Raise Error\nexcept NameError:\n    print\n    "An exception"\n    raise  # To determine whether the exception was raised or not'
>>> answer 3: raise NameError("Hi there")  # Raise Error
SyntaxError: invalid syntax
>>> def AbyB(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)

>>> AbyB(2.0, 3.0)
-5.0
>>> #Import error: It basically comes when we try to import any module that is not present.If python cannot find the module
>>> try:
    import abc
except ImportError:
    print("not abc")

>>> #Value error:It is raised when a built-in operation or function receives an argument that has the right type but an appropriate value
>>> while True:
    try:
        n = int(input("please,Enter a number:"))
        break
    except ValueError:
        print("You are supposed to enter a number!please try again...")
print("great,you successfully entered a number.")
SyntaxError: invalid syntax
>>> #Index error:It is raised whenever attempting to access an index that is outside the bounds of a list
>>> try:
    list = [1, 2]
    print(list[4])
except IndexError:
    print("This element can not be accessed.")

    
This element can not be accessed.
>>> class AgeTooSmallError(Exception):
    pass


def input_age():
    no = int(input("Enter the age:"))
    return no
SyntaxError: invalid syntax
>>> class AgeTooSmallError(Exception):
    pass

>>> def input_age():
    no = int(input("Enter the age:"))
    return no

>>> age = 18
>>> while True:
    try:
        no = input_age()
        if no < age:
            raise AgeTooSmallError
        else:
            print("Age correct...")
            break
    except AgeTooSmallError:
        print("error,Age is too small,enter again...")

        
Enter the age:10
error,Age is too small,enter again...
Enter the age:2
error,Age is too small,enter again...
Enter the age:
