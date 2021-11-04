class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if edges==[]:
            return True
        dic={}
        for edge in edges:
            if edge[0] not in dic:
                dic[edge[0]]=[edge[1]]
            else:
                dic[edge[0]].append(edge[1])
            if edge[1] not in dic:
                dic[edge[1]]=[edge[0]]
            else:
                dic[edge[1]].append(edge[0])
        print(dic)
        visited=set()
        def recur(start):
            ans=False
            if start==end:
                
                return True
            visited.add(start)
            for neighbor in dic[start]:
                
                if neighbor not in visited:
                    
                    ans=recur(neighbor) or ans
            return ans
        return recur(start)
                    
        
        
        
        
        
            
                