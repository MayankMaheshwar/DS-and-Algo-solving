
class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=0
        
        while n>0:
            i+=1
            if n-i<0:
                i-=1
                return i
            else:
                n-=i
        return i
            