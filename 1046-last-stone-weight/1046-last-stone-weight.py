class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        heapify(heap)
        for i in stones:
            heappush(heap,-1*i)
        while len(heap)>1:
            a=-1*heappop(heap)
            b=-1*heappop(heap)
            if a!=b:
                heappush(heap,-1*(abs(a-b)))
        if heap!=[]:
            return -1*heappop(heap)
        else:
            return 0
        