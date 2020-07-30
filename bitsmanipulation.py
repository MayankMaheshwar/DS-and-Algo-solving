# number is 21 and we use mask i.e. 0000 1111

def testbit(number,index):
    mask = 1 << index
    return (number & mask) != 0

def setbit(number,index):
    mask = 1 << index
    return number | mask

def clearbit(number,index):
    mask = 1 << index
    return number ^ mask


print(testbit(21,3))
print(clearortogglebit(21,2))

