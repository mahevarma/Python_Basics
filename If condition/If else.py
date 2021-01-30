"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

"""

a = 33
b = 200
if b > a:
    print("b is greater than a")

if a < b:
    print("a less than b")
else:
    print("a is greter than b")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

x = -1

if x>0 :
    if x==20:
        print("num is equal to 20")
    else :
        print("num not equal to 20")
else :
    print("Number is negative")

if 1:
    print("true")
else :
    print("false")