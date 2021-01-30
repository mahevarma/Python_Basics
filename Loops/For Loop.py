string = 'Python'

for character in string:
    print(character)

# Finding Nemo
fish_names = ['marlin', 'Dory', 'Nemo', 'Bloat', 'Bubbles']

i = 0
for fish in fish_names:
    if fish == "Nemo":
        print("Found Nemo ! at index location %d" % (fish_names.index('Nemo') + 1))
        i += 1
        print("number of attempts to find nemo %d" % i)
        break
    else:
        i += 1
        continue

for x in range( 101):
    if x % 4 == 0:
        print("Fizz")
    elif x % 8 == 0:
        print("Buzz")
    elif x % 12 == 0:
        print("Fizz Buzz")
    else:
        print(x)
