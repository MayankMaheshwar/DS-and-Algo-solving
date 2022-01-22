from collections import Counter
textInput = "cat matter cat matter safasf sfafsa"
arr = textInput.split()
print(arr)

c = Counter(arr)
print(c)
ans = []
for k, v in c.items():
    print(k, v)
    if v > 1:
        ans.append(k)

print(ans)
