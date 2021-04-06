a = 0
b = 0
c = 0
floor2 = 0
number = 0
floor1 = int(input("floor number"))
a = floor1
print("Lift a arrived")
while number == 0:
    floor2 = int(input('floor number'))

    if (abs(a-floor2)) <= abs(b-floor2) and abs(a-floor2) <= abs(c-floor2):
        a = floor2
        print('lift a arrived')
    else:
        if (abs(b-floor2)) <= abs(a-floor2) and abs(b-floor2) <= abs(c-floor2):
            b = floor2
            print('lift b arrived')
        else:
            c = floor2
            print('lift c arrived')
