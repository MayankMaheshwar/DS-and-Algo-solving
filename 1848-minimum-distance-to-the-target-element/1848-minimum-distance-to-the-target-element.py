class Solution:
    def getMinDistance(self, A: List[int], target: int, start: int) -> int:
        return min(abs(i - start) for i, a in enumerate(A) if a == target)
