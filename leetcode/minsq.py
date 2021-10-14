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
