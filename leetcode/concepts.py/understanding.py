"""def rotate(res, s, e):
    while s < e:
        res[s], res[e] = res[e], res[s]
        s += 1
        e -= 1


a = [1, 2, 3, 4, 5]
n = len(a)
rotate(a, 0, len(a)-1)
rotate(a, 0, n-2-1)
rotate(a, n-2, n-1)

print(a)
s = "agfsgadf"
print(list(reversed(s)))"""


def solve(A, B, C):

    dic = {}
    res = []
    for num in A:
        if num not in dic:
            dic[num] = 1

    for num in B:
        if num in dic and dic[num] == 1:
            dic[num] += 1

        else:
            dic[num] = 1

    for num in C:
        if num in dic and dic[num] >= 1:
            dic[num] += 1
    for k, v in dic.items():
        if v >= 2:
            res.append(k)
    print(dic)
    res.sort()
    print(res)


A = [56, 56, 34, 34, 72, 71]
B = [56, 56, 34, 34, 72, 71]
C = [56, 56, 34, 34, 72, 71]
solve(A, B, C)
