"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
"""


class Solution:
    def myAtoi(self, string: str) -> int:

        s = string.strip(" ")
        if len(s) == 0 or s == None:
            return 0

        neg = 0
        if s[0] in ("+", "-"):

            if s[0] == "-":
                neg = -1
            s = s[1:]
        elif not s[0].isdigit():
            return 0

        res = 0

        for i in range(len(s)):

            if noclass Solution:

    def myAtoi(self, string: str) -> int:

        s = string.strip(" ")
        if len(s) == 0 or s == None:
            return 0

        neg = 0
        if s[0] in ("+", "-"):

            if s[0] == "-":
                neg = -1
            s = s[1:]
        elif not s[0].isdigit():
            return 0

        res = 0

        for i in range(len(s)):

            if not s[i].isdigit():
                break
            else:
                val = int(s[i])
                res = res*10+val

        if neg == -1:
            res = res*(-1)
        if res < (-(2**31)):
            return -(2**31)

        if res > (2**31)-1:
            return (2**31)-1

        print(s)

        return res
