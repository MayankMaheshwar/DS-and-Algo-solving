# number is 21 and we use mask i.e. 0000 1111

def testbit(number,index):
    mask = 1 << index
    return (number & mask) != 0

def setbit(number,index):
    mask = 1 << index
    return number | mask

def clearortogglebit(number,index):
    mask = 1 << index
    return number ^ mask

def poweroftwo(number):
    return number & (number - 1) == 0

print(testbit(21,3))
print(clearortogglebit(21,2))

