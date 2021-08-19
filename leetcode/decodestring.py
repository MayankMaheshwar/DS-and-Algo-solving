class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s.startswith('0'):
            return 0
        wo_last, wo_last_two = 1, 1
        for i in range(1, len(s)):
            x = wo_last if s[i] != '0' else 0
            y = wo_last_two if int(
                s[i - 1: i + 1]) < 27 and s[i - 1] != '0' else 0
            wo_last = x + y
            wo_last_two = x
        return wo_last


" Another Solution "

class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[0]*n
      
        dp[0]=0 if int(s[0])==0 else 1
        if dp[0]==0:
            return 0
        
     
        for i in range(1,n):
            if int(s[i])>=1:
                dp[i]=dp[i-1]
                
            if int(s[i-1:i+1])>=10 and int(s[i-1:i+1])<=26:
                if i-2==-1:
                    dp[i]+=1
                else:
                    dp[i]+=dp[i-2]
        print(dp)
        return dp[n-1]
                