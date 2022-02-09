def gcd(x, y):
    while y:
        x, y = y, x % y
        print(x, y)

    return x


print(gcd(56, 98))
lcm = 98*56
print(lcm)
