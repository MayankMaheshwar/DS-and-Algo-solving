class Solution:
    def trailingZeroes(self, n: int) -> int:
        zc = 0
        while n > 0:
            n = n//5
            zc += n
            print(n, zc)
        return zc
