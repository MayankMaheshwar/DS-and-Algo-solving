arr = [8, 7, 4, 3, 1]
target = 5


def find(arr, target, start, end):

    if start == end:
        return -1
    mid = (start+end)//2
    if arr[mid] == target:
        return

    left = find(arr, target, start, mid-1)

    right = find(arr, target, mid+1, end)
    return max(left, right)


start = 0
end = len(arr)-1

print(find(arr, target, start, end))
