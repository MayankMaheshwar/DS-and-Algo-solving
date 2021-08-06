"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        d = collections.defaultdict(list)

        def dfs(node, height):
            d[height].append(node.val)
            for child in node.children:
                if child:
                    dfs(child, height+1)
        dfs(root, 0)
        return [d[height] for height in range(max(d)+1)]
