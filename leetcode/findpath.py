class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if edges == []:
            return True
        dic = {}
        for edge in edges:
            if edge[0] not in dic:
                dic[edge[0]] = [edge[1]]
            else:
                dic[edge[0]].append(edge[1])
            if edge[1] not in dic:
                dic[edge[1]] = [edge[0]]
            else:
                dic[edge[1]].append(edge[0])

        if start not in dic or end not in dic:
            return False

        if start in dic[end] or end in dic[start]:
            return True
        queue = deque()
        queue.append(start)
        visited = set()
        while queue:
            currentNode = queue.popleft()
            if currentNode == end:
                return True
            visited.add(currentNode)
            for neighbor in dic[currentNode]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return False
