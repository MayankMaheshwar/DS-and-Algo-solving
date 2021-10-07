arr1 = [-1, 3, 5, 10, 20, 28]
arr2 = [15, 17, 26, 28, 134, 135]
n1 = len(arr1)
n2 = len(arr2)
i = 0
j = 0
res = []
mx = 2**32
while j < n2 and i < n1:

    if abs(arr1[i]-arr2[j]) < mx:
        mx = abs(arr1[i]-arr2[j])
        res.append([arr1[i], arr2[j]])
    if arr1[i] > arr2[j]:
        j += 1
    else:
        i += 1
print(res[-1])
