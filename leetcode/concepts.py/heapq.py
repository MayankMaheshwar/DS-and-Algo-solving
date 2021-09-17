"""[summary]
1005. Maximize Sum Of Array After K Negations
Easy

718

66

Add to List

Share
Given an integer array nums and an integer k, modify the array in the following way:

choose an index i and replace nums[i] with -nums[i].
You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.


    """

import heapq


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:

        heapq.heapify(A)
        for _ in range(K):
            print("")
            heapq.heappush(A, -heapq.heappop(A))
            print(A)
        return sum(A)
