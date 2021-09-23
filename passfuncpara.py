def cal(sums):
    return sums()


def change(l):
    for i in range(len(l)):
        l[i] = 0


def sums():
    return 3+5


class cl:

    def __init__(self, list):
        self.list = list


list = [2, 3, 5, 43, 3]
obj = cl(list)
change(obj.list)
print(obj.list)
print(cal(sums))
