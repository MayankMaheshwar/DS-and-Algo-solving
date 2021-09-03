
def longSubarrWthSumDivByK(arr,  n, k):
    # Complete the function
    ms = 0

    l = 0
    r = n-1
    cusu = sum(arr)
    print(cusu)
    while l <= r:
        cur = cusu % k
        print(cur)
        if cur == 0:
            print(cusu % k)
            print(r, l)
            return r-l+1
        elif cusu-arr[l] % k == 0:

            l += 1
            print(r, l)
            return r-l+1

        elif cusu-arr[r] % k == 0:
            r -= 1
            return r-l+1
        else:
            cusu = cusu-arr[l]-arr[r]
            l += 1
            r -= 1

    return 1


print(longSubarrWthSumDivByK([1, 2, -2, 2, 2], 5, 2))
