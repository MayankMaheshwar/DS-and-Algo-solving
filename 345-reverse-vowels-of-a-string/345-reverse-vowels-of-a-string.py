class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="aAeEiIoOuU"
        l=0
        r=len(s)-1
        s=list(s)
        while l<r:
            if s[r] in vowels and s[l] in vowels:
                
                s[l],s[r]=s[r],s[l]
                
                l+=1
                r-=1
            elif s[l] in vowels:
                r-=1
            else:
                l+=1
        return "".join(s)
    
    