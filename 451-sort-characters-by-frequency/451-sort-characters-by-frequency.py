class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)
        d = sorted(c.items(),key=lambda x:x[1], reverse = True)
        ans=""
        for i in d:
            ans+=i[0]*i[1]
        return ans
            