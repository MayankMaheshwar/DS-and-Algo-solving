s = 'HackerEarth-$testing'
L = "%"
index = None
for i in range(len(s)):
    if L == s[i]:
        index = i
res = s[:index]
print(res, L, index)
