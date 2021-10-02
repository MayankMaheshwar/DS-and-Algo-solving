class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
    mi = 2**32
    A.sort()
    n = len(A)
    for i in range(1, n):

        res = A[i-1] ^ A[i]
        if res < mi:
            mi = res
    return mi
