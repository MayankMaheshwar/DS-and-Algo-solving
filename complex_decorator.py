import functools


def dwa(num):
    def d(func):
        @functools.wraps(func)
        def drf():
            print("inner")
            print(num)
            func()
            print("outer")
        return d
    return dwa


@dwa(89)
def func():
    print('beech')


func()
