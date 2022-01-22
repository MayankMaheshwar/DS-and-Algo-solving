data = str(data)
data = data.split()
n = len(data)
for i in range(n):
    data[i] = data[(i+k) % n]
print(data)
