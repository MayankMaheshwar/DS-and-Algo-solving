class Solution:
    @lru_cache(2000)
    def integerBreak(self, n: int) -> int:
        if n<=2:
            return 1
        ans = 1*(n-1)
        for i in range(2,n):
            fn=i
            sn=n-i
            p=fn*max(sn,self.integerBreak(sn))
            if p>ans:
                ans=p
        return ans
        