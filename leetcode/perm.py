from itertools import permutations
st = "kabccr"
s = list(set(st))

ans = list(permutations(s, 3))

a = []
for si in ans:
    a.append("".join(si))


b_list = sorted(a, key=str.lower)
print(b_list)
