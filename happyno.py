class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        s.add(n)
        while n != 1:
            l = list(str(n))
            l = list(map(int, l))
            l = [i**2 for i in l]
            n = sum(l)
            if n in s:
                return False
            else:
                s.add(n)
        return True
