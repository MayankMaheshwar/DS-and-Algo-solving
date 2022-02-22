"""
Given stream of numbers, find the median. Simulate streaming of numbers in the code
Example: when stream has 3,1,5,4,2 -> median is 3
If the old stream is added two more elements 3,1,5,4,2,7,6 - median is 4
If the the stream is added with one more elements - 3,1,5,4,2,7,6,8
median is (4+5)/2
"""
from heapq import *


class MedianFinder:
    def __init__(self):
        # the smaller half of the list, max heap (invert min-heap)
        self.small = []
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2.0
        else:
            return self.large[0]


obj = MedianFinder()
obj.addNum(3)
obj.addNum(1)
obj.addNum(5)
obj.addNum(4)
obj.addNum(2)
print(obj.small, obj.large)
print(obj.findMedian())
