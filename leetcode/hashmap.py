class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        Hash1, Hash2, Hash3 = set(A), set(B), set(C)
        res = set()
        for i in Hash1:
            if i in Hash2 or i in Hash3:
                res.add(i)
        for j in Hash2:
            if j in Hash3:
                res.add(j)

        return sorted(list(res))
