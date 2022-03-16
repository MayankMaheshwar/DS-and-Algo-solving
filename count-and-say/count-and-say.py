class Solution:
    def countAndSay(self, n: int) -> str:
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
            
        