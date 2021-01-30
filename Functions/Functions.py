# """
# What is a function in Python?
# In Python, a function is a group of related statements that performs a specific task.
#
# Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.
#
# Furthermore, it avoids repetition and makes the code reusable.
# """
#
#
# def greet(name):
#     """
#     This function greets to
#     the person passed in as
#     a parameter
#     """
#     print("Hello, " + name + ". Good morning!")
#
#
# greet("John")
#
#
# def arthemetic(x, y, operation):
#     if operation == 'add':
#         return x + y
#     elif operation == 'substract':
#         return x - y
#     elif operation == 'multipy':
#         return x * y
#     else:
#         "No operation specified"
#
#
# print(arthemetic(5, 5, 'add'))
# print(arthemetic(5, 12, 'substract'))
# print(arthemetic(5, 12, 'multipy'))
#
#
# def ex(y, x=10):
#     return x + y
#
#
# print(ex(5))
# print(ex(x=3, y=3))


# variable length arguments

def add(*x):
    sum = 0
    for num in x:
        sum += num
    return sum


print(add(1, 2, 3, 4))
