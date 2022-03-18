class Solution:
    def smallestSubsequence(self, S: str) -> str:
        last = {c: i for i, c in enumerate(S)}
        stack = []
        for i, c in enumerate(S):
            if c in stack: 
                print(stack,"con")
                continue
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
            print(stack,'end')
        return "".join(stack)