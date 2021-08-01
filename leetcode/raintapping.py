class Solution:
    def trap(self, height: List[int]) -> int:
        if height==[]:
            return 0
        mx=max(height)
        
        mxi=height.index(mx)
       
        tw=0
        lm=0
        for i in range(mxi):
            lm=max(lm,height[i])
            tw+=min(lm,mx)-height[i]
        
        lm=0
        for i in range(len(height)-1,mxi,-1):
            lm=max(lm,height[i])
            tw+=min(lm,mx)-height[i]
        return tw