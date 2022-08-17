class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftarr=[1]
        for i in range(0,len(nums)-1):
            leftarr.append(leftarr[i]*nums[i])
        rightproduct=1
        for i in range(len(nums)-1,-1,-1):
            
            leftarr[i]=leftarr[i]*rightproduct
            rightproduct*=nums[i]
           
        return leftarr