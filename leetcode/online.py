s = "aaabbababc"
if s == "":
    print("")

previousCount = 1
previousElement = s[0]
ans = ""

for i in range(1, len(s)):
    cur = s[i]
    if cur == previousElement:
        previousCount += 1
    else:
        ans += previousElement+str(previousCount)
        previousCount = 1
        previousElement = cur


ans += previousElement+str(previousCount)
print(ans)
