"""
Dictionary creation.
"""

empty = {}
print(empty)

simple_dictiornary = {1: 2}
print(simple_dictiornary)

squares = {1: 1, 2: 4, 3: 9, 4: 16}
print(squares)

cipher = {'p': 'o', 'y': 'h', 't': 'n',
          'h': 't', 'o': 'y', 'n': 'p'}
print(cipher)

goodinstructors = {'Rixner': True, 'Warren': False}
print(goodinstructors)

cities = {'China': ['Shanghai', 'Beijing'],
          'USA': ['New York', 'Los Angeles'],
          'Spain': ['Madrid', 'Barcelona'],
          'Australia': ['Sydney', 'Melbourne'],
          'Texas': ['Houston', 'San Antonio']}
print(cities)

''' 2 way of creating dictionaries '''

empty2 = dict()
print(empty2)

example = [(1, "one"), (2, "Two"), (3, "Three")]
names = dict(example)
print(names)





