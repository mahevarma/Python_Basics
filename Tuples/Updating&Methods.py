# Accessing elements of a Tuple

example = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(example[1])
print(example[:5])

# Updating the data inside a Tuple
example_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# we cannot change the data inside tuple as Tuples are immutable, how ever if there is a list inside a tuple we can
# update the list inside a tuple

example_tuple = (1, 2, 3, [1, 2, 4])
example_tuple[3][0] = 10
print(example_tuple)

# we cannot delete the elements inside a tuple, how ever we can delete entire tuple

example_tuple = (1, 2, 3, [1, 2, 4])
del example_tuple
# print(example_tuple)  # This gives error as we deleted Tuple

new_tuple = (1, 3, 5, 7, 8)
print(len(new_tuple))
print(max(new_tuple))
print(min(new_tuple))

# Tuple Swap
# Swap vales to x = 20 & y = 10
x = 10
y = 20

# In other languages we take help of third variable to swap values
z = x
x = y
y = z
print(x, y)

# Python way ( In python assignments are evaluated from right to left
# example x = 10 here it means a value 10 is assigned to a x

y, x = y, x
print(x, y)
