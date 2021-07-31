\"\"\"sumary_line
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.
\"\"\"


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        s = s.rstrip()
        if len(s) == 0:
            return l
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                return l
            l += 1
        return l
