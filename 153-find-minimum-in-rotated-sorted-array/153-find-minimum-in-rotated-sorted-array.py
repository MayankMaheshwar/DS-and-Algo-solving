class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while nums[left] > nums[right]:
            middle  = (left + right) // 2
            print(middle)
            if nums[middle] >= nums[left]:
                
                left=middle+1
            else:
                
                right=middle
        return nums[left]
        