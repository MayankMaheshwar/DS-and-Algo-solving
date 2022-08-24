import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        hq.heapify(stones)
        while len(stones)>1:
            f=hq.heappop(stones)
            s=hq.heappop(stones)
            hq.heappush(stones,f-s)
        stones.append(0)
        return stones[0]*(-1)
        