class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ml=2**32
        n=len(nums)
        cusu=0
        j=0
        for i in range(n):
            if nums[i]>=target:
                return 1
            cusu+=nums[i]
            
            if cusu>=target:
                
                while cusu-nums[j]>=target:
                    cusu-=nums[j]
                    j+=1
                if i-j+1<ml:
                    ml=i-j+1
                
            
        return ml if ml!=2**32 else 0