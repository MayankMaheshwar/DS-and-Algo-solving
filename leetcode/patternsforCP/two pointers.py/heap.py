import heapq
class Solution:
    #Function to return k largest elements from an array.
    def kLargest(self,li,n,k):
        # code here
        if li==[]:
            return []
        heapq._heapify_max(li)
        arr=heapq.nlargest(k,li)
        return arr