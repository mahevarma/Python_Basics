"""
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data
"""

# Creating a List
list_example = [1, 2, 'apple', 'ball']

# adding a element to a list
list_example.append("John")
list_example.insert(-1, "s")

print(list_example)

# list indexing
print(list_example[0])
print(list_example[0:3:2])  # 2 steps

# Adding two lists
x = [1, 2]
y = [3, 4]

z = x + y
print(z)

# Practice
list_1 = [1, 2, 3, 4, 5]
list_2 = ['A', 'B', 'C', 'D']
nested_list = [1, [2, 3, 4], 2]

# append
list_1.append(6)
print(list_1)

# remove
list_1.remove(5)
print(list_1)

# Pop
print("Removed element is ", list_1.pop())
print()

# sort
random_list = [1, 5, 3, 2]
random_list.sort()
print(random_list)

# delete
del random_list
print(random_list)

