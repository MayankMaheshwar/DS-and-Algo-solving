#  args helps to add unlimited numbers as a list
def arg(*args):
    return sum(args)


print(arg(3, 3433, 34252, 43, 53, 32, 4))

# kwargs helps to add key-value pairs as a set


def kwarg(**kwargs):
    print(kwargs)


kwarg(name='mayank', marks=89)
