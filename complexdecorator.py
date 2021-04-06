import functools


def decoarg(num):
    def mydec(func):
        @functools.wraps(func)
        def fun():
            print('in')
            if num == 56:
                func()
            else:
                print('not matched')
            print('out')
        return fun
    return mydec


@decoarg(56)
def func():
    print('Hello')


func()
