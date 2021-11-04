def dfs(graph,s):
    visited=set()
    def recur(s):
        visited.add(s)
        for neighbor in graph[s]:
            print(neighbor)
            if neighbor not in visited:
                recur(neighbor)
    
    recur(s)
    return visited


graph={0:[1,2],1:[0,2,4],2:[0,1,3],3:[2],4:[1]}
print(dfs(graph,0))



