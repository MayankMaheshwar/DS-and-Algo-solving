lift1 = 0
lift2 = 0
lift3 = 0
floors = 14

UserInput = 0

while UserInput <= 3:
    floorno = int(input('enter the floor'))
    UserInput += 1
    if UserInput == 1:
        lift1 = floorno
        print('lift1')
    elif abs(lift1-floorno) > lift2 or abs(lift1-floorno) > lift3:
        lift1 = floorno
        print('lift1')
    elif abs(lift2-floorno) > lift1 or abs(lift2-floorno) > lift3:
        lift2 = floorno
        print('lift2')
    else:
        lift3 = LookupError
        print('lift3')
