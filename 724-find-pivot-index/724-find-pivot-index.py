class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightsum=sum(nums)
        n=len(nums)
        leftsum=0
        i=0
        while i<n:
            rightsum-=nums[i]
            if leftsum==rightsum:
                return i
            else:
                leftsum+=nums[i]
            
            
            
            i+=1
        return -1