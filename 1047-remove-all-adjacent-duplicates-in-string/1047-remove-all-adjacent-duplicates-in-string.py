class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[s[0]]
        for i in range(1,len(s)):
            if stack==[]:
                stack.append(s[i])
            elif stack[-1]==s[i]:
                stack.pop()
            else:
                stack.append(s[i])
                
            
                
                
            
            
        return "".join(stack)
                