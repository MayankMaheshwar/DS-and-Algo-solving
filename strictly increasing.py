def merge(left, right, arr, count):
    l = r = k = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            arr[k] = left[l]
            l += 1
        else:
            count += 1
            arr[k] = right[r]
            r += 1
        k += 1
   
    while l < len(left):
        arr[k] = left[l]
        k += 1
        l += 1
    
    while r < len(right):
        arr[k] = right[r]
        k += 1
        r += 1
        
def almostIncreasingSequence(arr):
    if len(arr) <= 1:
        return arr
    count = 0
    mid = len(arr) // 2
    left = almostIncreasingSequence(arr[:mid])
    right = almostIncreasingSequence(arr[mid:])
    
    merge(left, right, arr, count)
    return arr

if __name__ == "__main__":
    arr=[1,3,2,1]
    print(almostIncreasingSequence(arr))