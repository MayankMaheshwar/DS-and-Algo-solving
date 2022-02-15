a = [2, 5, 8, 10]
b = [8, 3, 6, 11]
c = [2, 11, 8, 20, 343, 214, 2]


def unique(a, b, c):
    arr = [False]*(10**5)

    for num in a:
        arr[num] = True

    for num in b:
        arr[num] = True

    for num in c:
        arr[num] = True

    ans = []
    for i, num in enumerate(arr):
        if num == True:
            ans.append(i)
    return ans
