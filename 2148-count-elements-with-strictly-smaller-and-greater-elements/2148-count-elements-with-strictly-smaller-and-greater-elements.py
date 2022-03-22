class Solution:
    def countElements(self, nums: List[int]) -> int:
        mx=mn=nums[0]
        for el in nums:
            mx=max(mx,el)
            mn=min(mn,el)
        return sum(mn<el<mx for el in nums)