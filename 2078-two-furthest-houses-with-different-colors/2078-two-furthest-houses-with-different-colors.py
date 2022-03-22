class Solution:
    def maxDistance(self, A: List[int]) -> int:
        res = 0
        for i, x in enumerate(A):
            if x != A[0]:
                res = max(res, i)
            if x != A[-1]:
                res = max(res, len(A) - 1 - i)
        return res