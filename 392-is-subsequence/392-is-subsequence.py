class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        iss,it=0,0
        while it<len(t):
            if s[iss]==t[it]:
                iss+=1
                if iss==len(s):
                    return True
            it+=1
        return False    
        
            