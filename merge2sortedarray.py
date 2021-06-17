def merge(nums1, m, nums2, n):
    if m == 0:
        nums1[:] = nums2[:]
        return
    if n == 0:
        return nums1

    m = m-1
    n = n-1
    total = len(nums1)-1

    while (m >= 0) and (n >= 0):
        if nums1[m] > nums2[n]:
            nums1[total] = nums1[m]
            m -= 1
            total -= 1
            print(nums1, 'i')
        else:
            nums1[total] = nums2[n]
            n -= 1
            total -= 1
            print(nums1, 'e')

    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
print(3 > 3)
print(merge(nums1, 3, nums2, len(nums2)))
