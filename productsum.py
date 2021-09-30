sum = 0


def sol(arr, mul, cur, start):
    global sum
    if start == len(arr)-1:
        cur += arr[start]
        cur = cur*mul
        sum += cur
        print(cur)
        return cur
    if type(arr[start]) == list:
        mul += 1
        cur = 0

        cur += sol(arr[start], mul, cur, start=0)

    else:
        cur += arr[start]

    start += 1

    return sol(arr, mul, cur, start)


if __name__ == '__main__':
    arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    mul = 1

    start = 0
    cur = 0
    print(sum)
    print(sol(arr, mul, cur, start))
