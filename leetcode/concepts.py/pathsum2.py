class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums = list(accumulate(nums))
        c = 0
        for i in nums:
            r = 0
            if i == k:
                c += 1
            while i >= k:
                i -= nums[r]
                r += 1

                if i == k:
                    c += 1
        return c
