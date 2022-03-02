class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        iss,it=len(s)-1,len(t)-1
        while it>=0:
            if t[it]==s[iss]:
                iss-=1
                
                if iss==-1:
                    
                    return True
            it-=1
            
        return False    
        
            