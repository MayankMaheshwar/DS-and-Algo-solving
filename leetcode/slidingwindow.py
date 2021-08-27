class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        ma = 0

        cursum = sum(nums[:k])

        ma = cursum/k
        for i in range(k, len(nums)):
            cursum += nums[i]
            cursum -= nums[i-k]
            av = cursum/k
            if av > ma:
                ma = av
        return ma
