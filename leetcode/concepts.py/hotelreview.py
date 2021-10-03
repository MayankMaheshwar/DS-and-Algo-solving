
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


class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        goodWords = set(A.split("_"))
        # Making it into a set is important, as searching through a set is faster
        V = []
        for index in range(len(B)):
            countGoodWords = 0
            for word in B[index].split("_"):
                if word in goodWords:
                    countGoodWords += 1
            V.append([index, countGoodWords])  # store the index and the count
        # use the count to sort (descending order)
        V.sort(key=lambda a: a[1], reverse=True)
        return [x[0] for x in V]  # return the sorted list of indexes

        ans = []
        for key, value in sorted(dict.items(), key=lambda item: item[1], reverse=True):
            ans.append(key)
        return ans
