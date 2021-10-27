from collections import Counter as cp
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c=cp(nums)
        c=sorted(c.items(),key=lambda x:-x[1])
        ans=[]
        for i in range(k):
            ans.append(c[i][0])
        return ans
            