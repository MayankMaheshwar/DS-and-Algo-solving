from collections import deque
def dfs(graph,sn,en):
    nodesvisit=deque([sn])
    nodesseen=set()
    
    while len(nodesvisit)>0:
        cur = nodesvisit.popleft()
        for neighbor in graph[cur]:
            if neighbor not in nodesseen:
                nodesvisit.append(neighbor)
                nodesseen.add(neighbor)
    return nodesseen





graph={'c':['a','e','d','f'],'b':['a'],'a':['b','c'],'e':['c'],'d':['c','g'],'g':[],'f':[]}
print(dfs(graph,'c','h'))