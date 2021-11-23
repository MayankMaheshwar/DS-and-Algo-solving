n = len(nums)
  left, right = 0, n - 1
   while left <= right:
        mid = (left + right) // 2
        if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == n-1 or nums[mid] > nums[mid+1]):  # Found peak
            return mid
        if mid == 0 or nums[mid-1] < nums[mid]:  # Find peak on the right
            left = mid + 1
        else:  # Find peak on the left
            right = mid - 1
    return -1
