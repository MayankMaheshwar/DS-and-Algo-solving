

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapp = {}
        boo = {}
        for i in range(len(s)):
            if s[i] in mapp and mapp[s[i]] != t[i]:
                return False
            elif t[i] in boo and s[i] not in mapp:
                return False

            else:
                boo[t[i]] = True
                mapp[s[i]] = t[i]
        return True
