class Solution:
    def romanToInt(self, s: str) -> int:
        
        d={'I'        :    1,
'V'       :      5,
'X'       :      10,
'L'       :      50,
'C'       :      100,
'D'        :     500,
'M'        :     1000}
        
        if len(s)==1:
            return d[s]
        i=len(s)-1
        am=0
        while i>=0:
            if i==0:
                am+=d[s[i]]
                return am
            if d[s[i]]>d[s[i-1]]:
                am+=d[s[i]]-d[s[i-1]]
                i-=2
                
            else:
                
                am+=d[s[i]]
                i-=1
        return am
       
                
            
        