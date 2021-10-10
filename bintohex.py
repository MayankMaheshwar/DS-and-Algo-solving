"""
Two's complement:
Step 1: Transforming 0 to 1 and 1 to 0
Step 2: plus 1

for example: (8-bits) '11111111' and num = -1
Step 1 can become: '11111111' + num = '11111111' - '1' = '11111110'
Step 2: '11111110' + '1' = '11111111'
actually '11111111' = 2 ** 8 -1
so we can simplify step 1 and step 2 to : 2 ** 8 - 1 + num +1 = 2 ** 8 + num
"""


class Solution:
    def toHex(self, num: int) -> str:
        s, res, num = '0123456789abcdef', '', num & 0xFFFFFFFF
        while num:
            res += s[num % 16]
            num >>= 4

        return res[::-1] or '0'
