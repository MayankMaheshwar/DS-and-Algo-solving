n = 21
a = 0
b = 1


def reverse(a, b, n):
    if b == n:
        print(b, end=" ")
    reverse(b, a+b, n)
    print(a, end=" ")


reverse(a, b, n)
