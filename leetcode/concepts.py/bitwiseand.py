class Solution:
    def rangeBitwiseAnd(self, n: int, m: int) -> int:
        while(m > n):
            m = m & (m-1)
        return m
