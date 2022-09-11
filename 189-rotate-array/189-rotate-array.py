class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k==0:
            return nums
        
        
        def rl(nums,start,end):
            while start<end:
                nums[start],nums[end] = nums[end], nums[start]
                start+=1
                end-=1
        
        rl(nums,0,len(nums)-1)
        if k>len(nums):
            k=k%len(nums)
        rl(nums,0,k-1)
        rl(nums,k,len(nums)-1)
        return nums