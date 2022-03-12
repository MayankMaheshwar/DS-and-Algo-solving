class Solution(object):
    def generateParenthesis(self, n):
        def generate(A,o,c):
            
            if len(A) == 2*n:
                
                ans.append(A)
                return
            if o<n:
                generate(A+'(',o+1,c)
            if c<o:
                generate(A+')',o,c+1)
                

        ans = []
        a='('
        generate(a,1,0)
        return ans