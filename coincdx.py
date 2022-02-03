""" Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.

example: Input: num = "143392", k = 3
Output: "32"

"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and len(stack) > 0 and stack[-1] > digit:
                k -= 1
                stack.pop()
            stack.append(digit)

        if k > 0:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"
