from functools import reduce
l = [1, 23, 45, 5, 3, 532, 34, 35, 3]
l = list(filter(lambda x: x % 2 == 0, l))
print(l)

l = [1, 23, 45, 5, 3, 532, 34, 35, 3]
s = reduce(lambda x, y: x+y, l)
print(s)
