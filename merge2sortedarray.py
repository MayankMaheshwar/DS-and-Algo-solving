
def merge(nums1, m, nums2, n):
    if m == 0:
        nums1[:] = nums2[:]
        return
    if n == 0:
        return nums1

    m = m-1

    n = n-1
    total = len(nums1)-1

    while (n >= 0) or (m >= 0):
        if nums1[m] > nums2[n]:
            nums1[total] = nums1[m]
            m -= 1
            total -= 1

        else:
            nums1[total] = nums2[n]
            n -= 1
            total -= 1
        print(m, n)

    if n >= 0:
        nums1[:total+1] = nums2[:n+1]

    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
print(merge(nums1, 3, nums2, len(nums2)))
