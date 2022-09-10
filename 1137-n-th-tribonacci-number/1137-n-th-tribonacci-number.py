class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        a,b,c=0,1,1
        for i in range(2,n):
            temp=a+b+c
            a,b,c=b,c,temp
        return c
            
        