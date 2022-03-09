class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0,1]
        j = 1
        for i in range(2,n//2+2):
            nums.append(nums[j])
            nums.append(nums[j]+nums[j+1])
            j+=1
        return max(nums[:n+1])