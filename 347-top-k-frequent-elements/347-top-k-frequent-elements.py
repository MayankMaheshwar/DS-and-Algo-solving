from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c=Counter(nums)
        
        ans=[]
        h=[]
        for t,v in c.items():
            heapq.heappush(h,(-v,t))
        heapq.heapify(h)
        for i in range(k):
            q=heapq.heappop(h)
            ans.append(q[1])
        return ans
        