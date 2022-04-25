class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total=0
        diff=[]
        for x, y in costs:
            diff.append(y-x)
            total+=x
        
        diff.sort()
        
        for i in range(len(costs)//2):
            total+=diff[i]
        return total
    
   
        