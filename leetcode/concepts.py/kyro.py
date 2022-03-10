import random
arr = [i for i in range(100)]


def shuffle(arr):
    count = 0
    n = len(arr)

    while_count = 0
    while count != n:
        while_count += 1
        rand = random.randint(count, n-1)
        arr[count], arr[rand] = arr[rand], arr[count]
        count += 1

    print(while_count)
    return arr


print(shuffle(arr))
