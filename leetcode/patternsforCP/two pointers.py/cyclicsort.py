# Cyclic Sort - Time O(n) and space O(1)
 # Sort the array with Cyclic Sort
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        start, output = 0, []
        while start < len(nums):
                index = nums[start]-1

                if nums[index] != nums[start]:
                    nums[index], nums[start] = nums[start], nums[index]
                else:
                    start += 1
            for i, v in enumerate(nums):
                if i+1 != v:
                    output.append(i+1)
            return output
