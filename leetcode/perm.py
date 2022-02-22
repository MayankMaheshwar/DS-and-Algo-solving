from itertools import permutations
s = "kabccr"
ans = list(permutations(list(s), 3))
a = []
for st in ans:
    ans.append("".join(st))

print(sorted(ans))
