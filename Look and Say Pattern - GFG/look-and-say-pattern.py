#User function Template for python3
from itertools import groupby
class Solution:

    def lookandsay(self, n):
        # code here
        if n==1:
            return '1'
        k=1
        s='1'
        
        for i in range(1,n):
            res=''
            for k,v in groupby(s):
                
                res+=str(len(list(v)))+str(k) 
                
             
            s=res
        
        return s
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.lookandsay(n))

# } Driver Code Ends