class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        ch=math.log(n,4)
        print(ch)
        if int(ch)==0:
            return False
        return not int(ch)%ch