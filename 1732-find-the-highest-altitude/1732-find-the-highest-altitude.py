class Solution:
    def largestAltitude(self, A: List[int]) -> int:
        return max(0, max(accumulate(A)))
