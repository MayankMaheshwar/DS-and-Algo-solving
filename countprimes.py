
class Solution:
    def countPrimes(self, n: int) -> int:
        check = [True for _ in range(n)]
        p = 2
        ans = 0
        while p*p <= n:
            if check[p]:
                for i in range(p*p, n, p):
                    check[i] = False

            p += 1

        ans = sum([True for i in range(2, n) if check[i] == True])

        return ans
