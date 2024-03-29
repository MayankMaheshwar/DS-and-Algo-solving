# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while True:
            mid = (l+r) >> 1
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                r = mid-1
            else:
                l = mid+1
