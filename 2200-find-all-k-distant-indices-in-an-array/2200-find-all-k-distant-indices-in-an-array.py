class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        I = []
        start, stop = 0, len(nums)
        for i, num in enumerate(nums):
            if num == key:
                I += range(max(i-k, start),
                           min(i+k+1, stop))
                start = i+k+1
        return I