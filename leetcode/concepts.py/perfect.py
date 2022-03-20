from datetime import datetime
n = 100000
ans = []


now = datetime.now()
for num in range(6, n+1):
    cur = 0
    for div in range(1, num//2+1):
        if num % div == 0:
            cur += div

    if cur == num:
        ans.append(cur)
end = datetime.now()

print(ans)
print(end-now)
