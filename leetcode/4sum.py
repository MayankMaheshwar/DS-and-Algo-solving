""" 
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.


"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        i = 0
        while i < (len(nums)-3):
            j = i+1
            while j < (len(nums)-2):
                required = target-(nums[i]+nums[j])
                left = j+1
                right = n-1

                while left < right:
                    two_sum = nums[left]+nums[right]
                    if two_sum > required:
                        right -= 1
                    elif two_sum < required:
                        left += 1
                    else:
                        quad = []
                        quad.append(nums[i])
                        quad.append(nums[j])
                        quad.append(nums[left])
                        quad.append(nums[right])
                        res.append(quad)
                        while left < right and nums[left] == quad[2]:
                            left += 1
                        while right > left and nums[right] == quad[3]:
                            right -= 1

                while j < n-3 and nums[j] == nums[j+1]:
                    j += 1
                j += 1

            while i < n-4 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res
