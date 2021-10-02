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


A = [15, 5, 1, 10, 2]
mi = 2**32
for i, num in enumerate(A):
    if i == len(A)-1:
        break
    if A[i+1] ^ num < mi:
        mi = A[i+1] ^ num
print(5 ^ (-5))
