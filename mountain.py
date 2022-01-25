class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        flag = 0
        for i in range(len(A)-1):
            if A[i] == A[i+1]:
                return False
            if flag == 0:

                if A[i] > A[i+1]:
                    flag = 1
            else:
                if A[i] < A[i+1]:
                    return False
        return True if A[-2] > A[-1] and A[0] < A[1] else False
