class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ans = 26*96
        ans += (26*(26+1))//2
        res = 0
        for i in set(sentence):
            res += ord(i)
        print(res, ans)
        return ans == res
