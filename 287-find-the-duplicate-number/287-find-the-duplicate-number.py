class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start=0
        while start<len(nums):
            index = nums[start]-1
            
            if nums[index]!=nums[start]: 
                nums[index], nums[start] = nums[start], nums[index]
                
            else:
                start+=1
          
        return nums[-1]