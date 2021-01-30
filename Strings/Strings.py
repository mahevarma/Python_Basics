# Strings in python are surrounded by either single quotation marks, or double quotation

a = "Hello world"
b = 'Hello World'
c = "hello's World"

print(a, b, c, sep=" |")
print(a * 4)
print(a * -1)  # Dont multipy with negative number => In this case phyton will retun empty string

# Indexing

# Indexing is the postion of the character in the string

# 0  1 2 3 4
# H  e l l o
# -5-4-3-2-1

x = "Hello"
print(x[0])

""" concatenating the string"""

string_one = "Hi"
String_two = "how are you?"

print(string_one + "," + " " + String_two)

# Slicing
""" Slicign is the process of extracting substring from a string using the index
To extact a substring from string s from index m to index n

Expression:-s[m:n+1]
# why n+1 ? because python doesnt include the end index while slicing     
"""
x = "Hello"
z = '12345' * 5

print(x[0:5:2])  # 2 steps away
print(z[::5])

# functions on string
x = "1,2,3,4,5"
y = "Hello"
print(x.replace("2", "3"))
print(len(x))
print(y.upper())
print(y.lower())
print(y.title())
