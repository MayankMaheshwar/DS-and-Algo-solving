arr = [5, 43, 2, 46, 3, 2, 4, 96, 5, 1, 1]

for i in range(1, len(arr)):
    j = i
    while arr[j] < arr[j-1] and j > 0:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1
print(arr)
