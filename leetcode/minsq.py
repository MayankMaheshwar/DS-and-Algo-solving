class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 3:
            return n
        dp = [2**32]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n+1):
            mi = 10**4+1
            end = int(i**0.5)+1
            for j in range(1, end):
                rem = i-(j*j)
                mi = min(mi, dp[rem])
            dp[i] = mi+1

        return dp[n]


class Solution:
    def numSquares(self, n: int) -> int:
        if int(sqrt(n))**2 == n:
            return 1
        for j in range(int(sqrt(n)) + 1):
            if int(sqrt(n - j*j))**2 == n - j*j:
                return 2

        while n % 4 == 0:
            n >>= 2
        if n % 8 == 7:
            return 4
        return 3
