class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        
        maxHeap = [-v for v in freq.values()]
        t=0
        heapq.heapify(maxHeap)
        q=deque()
        while maxHeap or q:
            t+=1
            if maxHeap:
                cnt = 1+ heapq.heappop(maxHeap)

                if cnt!=0:
                    q.append([cnt,t+n])
            if q and q[0][1]==t:
                heapq.heappush(maxHeap,q.popleft()[0])
        return t
                
            
             
        