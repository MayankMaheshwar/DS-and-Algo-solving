n = int(input())
m = int(input())
matrix = []
for i in range(n):
    col = list(map(int, input().split()))
    matrix.append(col)

q = int(input())
s = int(input())
query = []
for i in range(q):
    q = list(map(int, input().split()))
    query.append(q)

sums = []

for i in range(0, n):
    sumRow = 0
    for j in range(0, m):
        sumRow = sumRow + matrix[i][j]  
    sums.append(sumRow)

for i in range(0, n):
    sumCol = 0
    for j in range(0, m):
        sumCol = sumCol + matrix[j][i]
    sums.append(sumCol)

for j in query:
    ans = 0
    for i in range(len(sums)):

        if sums[i] >= j[0] and sums[i] <= j[1]:
            ans += 1
    print(ans, end=" ")
