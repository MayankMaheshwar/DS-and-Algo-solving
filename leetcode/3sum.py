class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) < 3:
            return res
        n = len(nums)
        nums.sort()
        i = 0
        while i < n-2:

            left = i+1
            right = n-1
            while left < right:

                if nums[i]+nums[left]+nums[right] == 0:
                    res1 = [nums[i]]
                    res1.append(nums[left])
                    res1.append(nums[right])
                    left += 1
                    right -= 1
                    res.append(res1)
                    while left < right and nums[left] == res1[1]:

                        left += 1
                    while right > left and nums[right] == res1[2]:
                        right -= 1

                elif nums[i]+nums[left]+nums[right] > 0:
                    right -= 1
                else:
                    left += 1
            while i < n-3 and nums[i] == nums[i+1]:
                i += 1
            i += 1

        return res
