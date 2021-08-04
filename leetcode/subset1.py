class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(1, 2**len(nums)):
            ans = []
            st = bin(i)[2:].zfill(len(nums))
            for i in range(len(st)):
                if st[i] == '1':
                    ans.append(nums[i])
            res.append(ans)
        return res
