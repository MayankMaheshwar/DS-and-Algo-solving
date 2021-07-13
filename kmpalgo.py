"""KMP ALgorithm """


class Solution:
    def lpsm(self, s):
        n = len(s)
        lps = [0]*n
        le = 0
        i = 1
        while i < n:
            if s[i] == s[le]:
                lps[i] = le+1
                le += 1
                i += 1

            else:
                if le != 0:
                    le = lps[le-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if haystack == "":
            return -1
        if needle == haystack:
            return 0

        arr = self.lpsm(needle)
        t = 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[t]:
                t += 1
                i += 1

            else:
                if t != 0:
                    t = arr[t-1]
                else:
                    i += 1
            if t == len(needle):
                return i-t
        return -1
