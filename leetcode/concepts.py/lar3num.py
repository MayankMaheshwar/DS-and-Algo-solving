arr = [2, 3, 1, 4534, 3, 4, 545, 3333333333333, 43, 463, 213]
a = 0
b = 0
c = 0
for num in arr:
    if num > c:
        a = b
        b = c
        c = num
    elif num > b and num < c:
        a = b
        b = num
    elif num > a and num < b:
        a = num
print(c)
