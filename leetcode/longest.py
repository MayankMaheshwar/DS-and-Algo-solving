from collections import deque
list = ['a-b', 'b-c', 'b-d']
dic = {}
unique = []
for edge in list:
    if edge[0] not in unique:
        unique.append(edge[0])
    if edge[2] not in unique:
        unique.append(edge[2])
    if edge[0] not in dic:
        dic[edge[0]] = [edge[2]]
    else:
        dic[edge[0]].append(edge[2])
    if edge[2] not in dic:
        dic[edge[2]] = [edge[0]]
    else:
        dic[edge[2]].append(edge[0])

mx = 0
for node in unique:

    queue = deque()  
    visited = set()
    queue.append(node)
    while queue:
        curnode = queue.popleft()
        visited.add(curnode)
        for neighbor in dic[curnode]:
            if neighbor not in visited:
                queue.append(neighbor)
    print(visited)
    if len(visited)-1 > mx:
        mx = len(visited)-1

print(mx)
