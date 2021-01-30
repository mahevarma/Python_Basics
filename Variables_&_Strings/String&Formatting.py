""""
A Python variable is a reserved memory location to store values.
In other words, a variable in a python program gives data to the computer for processing.
"""
x = 100
y = 200
my_name = "Mahesh"
variale_boolean = True

print("My name is :", my_name)

# String Formatting
# 1 “Old Style” String Formatting (% Operator)

"""
Here are some basic argument specifiers you should know:

%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)

"""

name = 'Bob'
print('Hello, my name is', name)

name = "John"
dog_name = "benny"
age = 23
print('%s is %d years old.' % (name, age))

first_num = 10
sec_num = 20
print("Fist num is %0.2f" % first_num)

# Format
print("My name is {} and my dog name is {}".format(my_name, dog_name))

name = "Python"
version = 3.7
print("Hi {name}, version {version}".format(name=name, version=version))


