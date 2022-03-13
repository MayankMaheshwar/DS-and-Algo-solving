class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack=[]
        d={"{":'}',"(":')',"[":']'}
        for i in s:
            if i in d:
                stack.append(i)
            if i not in d:
                if len(stack)==0:
                    return False
                elif d[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
        if len(stack)>0:
            return False
        else:
            return True
                