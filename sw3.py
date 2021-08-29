def x(t):
    z = t.swapcase()
    t = list(t)
    z = list(z)
    for c in t:
        if c not in z:
            return False
    return True


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        b = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                a = s[i:j+1]
                if x(a) and len(a) > len(b):
                    b = a
        return b
