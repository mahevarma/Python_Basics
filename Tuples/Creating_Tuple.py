# # # # # # # # # # # # # # # TUPLES # # # # # # # # # # # # # # #

# Tuples are Fixed lenght, Immutable data type in python
my_info = ('John', 27, "Chicago")

# Properties of a Tuple
# 1) Accessing elements is same as lists
# 2) Tuples are immputable

# Creating a tuple

tuple_example = (1, 2, 3, 4, 5)
print(type(tuple_example))

tuple_example = 1, 2, 3, 4, 5  # if we dont mention any data type, python stores it as Tuple
print(type(tuple_example))

name = "John"
print(tuple(name))
print(type(tuple(name)))

# Convert a List to a Tuple
list_example = [1, 2, 3, 4, 5]
print(type(tuple(list_example)))

# If we have 1 element in collection, metion "," otherwise python returns error (In this case it will return 1 (Integer)

tuple_ex = (1,)
print(tuple_ex)

# tuple unpacking
example = (10, 20)
x, y = example
print(type(x))
print(x)
print(y)
print(x, y)
