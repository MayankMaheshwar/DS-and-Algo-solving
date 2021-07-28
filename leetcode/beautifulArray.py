"""
For some fixed n, an array nums is beautiful if it is a permutation of the integers 1, 2, ..., n, such that:

For every i < j, there is no k with i < k < j such that nums[k] * 2 = nums[i] + nums[j].

Given n, return any beautiful array nums.  (It is guaranteed that one exists.)

"""


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        sample = [1]
        if n == 1:
            return sample
        for i in range(1, n):
            odd = []
            even = []
            l = len(sample)
            i = 0
            while i < l:
                odd1 = (sample[i]*2)-1
                if odd1 <= n:
                    odd.append(odd1)
                even1 = sample[i]*2
                if even1 <= n:
                    even.append(even1)
                i += 1
            sample = odd+even
        return sample
