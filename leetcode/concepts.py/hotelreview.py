
class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        d = A.split("_")
        A = {}
        for w in d:
            A[w] = 1

        def gwc(x):
            ans = 0
            d = x.split("_")
            for y in d:
                if y in A:
                    ans += 1
            return ans

        l = len(B)
        for i in range(l):
            c = gwc(B[i])
            B[i] = [c, i]

        B.sort(key=lambda x: (-x[0], x[1]))

        return [x[1] for x in B]
