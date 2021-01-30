""" while loop is used for execting a block of statement as soon as condtion is True """
x = 10

while x > 5:
    print("x value is %d" % x)
    x += -1

while True:
    x = input("what is your name ?")
    if x != 'stop':
        print(x)
    else:
        print("user stopped")
        break
