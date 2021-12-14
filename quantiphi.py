from itertools import groupby
string = 'aaabbbbccccccaaa'

dic = {}
for chr in string:
    if chr in dic:
        dic[chr] += 1
    else:
        dic[chr] = 1


mx = -2**32
malpha = []
for k, v in dic.items():
    if v >= mx:
        mx = v
        malpha = k

print(mx, malpha)
