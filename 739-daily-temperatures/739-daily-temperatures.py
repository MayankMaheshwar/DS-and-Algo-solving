class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n=len(T)
        stack=[(T[n-1],n-1)]
        
        ans=[0]*n
        ans[n-1]=0
        
        
        for i in range(n-2,-1,-1):
            
            
            while stack[-1][0]<=T[i]:
                stack.pop()
                if stack==[]:
                    
                    
                    break
                
                
            if stack==[]:
                
                ans[i]=0
            else:
                ans[i]=stack[-1][1]-i
                
            stack.append((T[i],i))
            

            
        return ans
                
            
                
                
            
        
        