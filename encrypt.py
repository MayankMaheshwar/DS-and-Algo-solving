from collections import Counter
arr = textInput.split()


c = Counter(arr)
print(c)
ans = []
for k, v in c.items():

    if v > 1:
        ans.append(k)

print(ans)
