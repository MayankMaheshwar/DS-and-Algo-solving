class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        c=0
        for i in range(1,len(nums)):
            
            if nums[i-1]>=nums[i]:
                
                c+=1
                if i>1 and nums[i-2]>=nums[i]:
                    nums[i]=nums[i-1]
        return c<2
                
                
                
                
                
