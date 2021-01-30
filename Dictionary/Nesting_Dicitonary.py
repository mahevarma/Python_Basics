# A list of Dictionaries
alien_0 = {'color': 'Green', 'points': 1}
alien_1 = {'color': 'yellow', 'points': 3}
alien_2 = {'color': 'red', 'points': 5}

alieans = [alien_0, alien_1, alien_2]
for aliean in alieans:
    print(aliean)

# Example to create a fleet of 30 alieans
aliean = []
for aliean_number in range(30):
    new_aliean = {'color': 'red', 'points': 5, 'speed': 'Fast'}
    alieans.append(new_aliean)
num = 0
# Show first 5 Alieans
for aliean in alieans[:5]:
    print(str(num) + " aliean " + str(aliean))
    num += 1
# A list in a dictionary
pizza = {'crust': 'thick', 'toppings': ['Extra cheese', 'mushrooms', 'onions']}
print(pizza['crust'])
for toppings in pizza['toppings']:
    print(toppings)

Fav_languages = {'Mahesh': ['Python', 'Scala', 'VBA'], 'Tom': ['C'], 'John': ['C++', 'Ruby']}

for name, lang in Fav_languages.items():
    print("\n" + name.title() + "Fav language is :")
    for lng in lang:
        print(lng)

# A dictionary in Dictionary python

users = {'Mahesh': {'First': 'M',
                    'Last': 'V',
                    'location': 'hyderbad'}}
print(users['Mahesh']['First'])

