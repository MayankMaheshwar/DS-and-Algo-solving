class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                temp=nums[i]
                nums[i]=nums[i-1]+1
                c+=nums[i-1]-temp+1
        return c