# Adding a New Key-value pairs

person = {}
person['Name'] = 'Tom'
person['Age'] = 30
person['DOB'] = '1-1-1990'
person['Rank'] = 1

print(person)

# Update the dictionary value

person['Name'] = 'John'
print("The new name is " + person['Name'])

# Loop through Keys
for attribute in person.keys():
    print(attribute)

# Looping through Values
for attribute in person.values():
    print(attribute)
# Looping through all Key-Vlaue Pairs
for attribute in person.items():
    print(attribute)

# Change Person name to tom
if person['Name'] == "John":
    person['Name'] = 'Tom'
else:
    pass
print(person)

# Deleting a Dicitonary

dict_1 = {1: 'One', 2: 'two', 3: 'three'}
del dict_1
# print(dict_1)

dict_2 = {1: 'One', 2: 'two', 3: 'three'}

dict_2.pop(3)
print(dict_2)
dict_2.popitem()
print(dict_2)


