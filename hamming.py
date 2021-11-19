class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y
        ans = 0
        while res != 0:
            res = res & (res-1)
            ans += 1

        return ans
