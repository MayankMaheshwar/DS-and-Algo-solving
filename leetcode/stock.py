n = len(prices)
   if n <= 1:
        return 0

    diff = [prices[i+1] - prices[i] for i in range(n-1)]
    dp, dp_max = [0]*(n + 1), [0]*(n + 1)
    for i in range(n-1):
        dp[i] = diff[i] + max(dp_max[i-3], dp[i-1])
        dp_max[i] = max(dp_max[i-1], dp[i])

    return dp_max[-3]


"""free = 0
        have = cool = float('-inf')
        for p in prices:
            free, have, cool = max(free, cool), max(have, free - p), have + p
        return max(free, cool)"""
