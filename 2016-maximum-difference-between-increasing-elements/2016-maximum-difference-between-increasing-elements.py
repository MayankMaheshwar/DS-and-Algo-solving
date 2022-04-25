class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff, mi = -1, math.inf
        for i, n in enumerate(nums):
            if i > 0 and n > mi:
                diff = max(diff, n - mi)    
            mi = min(mi, n)
        return diff    