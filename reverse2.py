class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s)-1, k):
            s[i], s[i+1] = s[i+1], s[i]
            print(s[i], s[i+1])
        return "".join(s)
