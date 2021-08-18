class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s.startswith('0'):
            return 0
        wo_last, wo_last_two = 1, 1
        for i in range(1, len(s)):
            x = wo_last if s[i] != '0' else 0
            y = wo_last_two if int(
                s[i - 1: i + 1]) < 27 and s[i - 1] != '0' else 0
            wo_last = x + y
            wo_last_two = x
        return wo_last
