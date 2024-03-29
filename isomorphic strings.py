"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

"""


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
