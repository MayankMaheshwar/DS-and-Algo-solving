string = "BAANANAS"
v, c = set(), set()
lc, lv = 2**32, 2**32
string = string.lower()
for i in range(len(string)):
    if string[i] in ['a', 'e', 'i', 'o', 'u']:
        if lv > i:
            lv = i
        for j in range(i+1, len(string)):
            v.add(string[i:j])
            if j == len(string)-1:
                v.add(string[i:j+1])
    else:
        if lc > i:
            lc = i
        for j in range(i+1, len(string)):
            c.add(string[i:j])
            if j == len(string)-1:
                c.add(string[i:j+1])
lk = string[lv:]
v.add(lk)
ls = string[lc:]
c.add(ls)
kevin, stuart = 0, 0
for i in v:
    kevin += lk.count(i)
for i in c:
    stuart += ls.count(i)

if kevin > stuart:
    print("Kevin", kevin)
else:
    print("Stuart", stuart)
