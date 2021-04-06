def m(t):
    return t

@m
def t():
    return m("dgs")


print(t())