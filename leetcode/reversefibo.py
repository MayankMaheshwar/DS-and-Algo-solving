n = 21
a = 0
b = 1


def reverse(a, b, n):
    if b == n:
        print(b, end=" ")
        return

    reverse(b, a+b, n)
    print(a, end=" ")
    return


reverse(a, b, n)
