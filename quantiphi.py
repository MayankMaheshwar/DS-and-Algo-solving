from itertools import groupby
string = 'aaabbbbcccccaaa'
obj = groupby(string)
max = -2**32
malpha = ""

for k, v in obj:
    if len(list(v)) > max:
        max = len(v)
        malpha = k

print(malpha)
