"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root==None:
            return None
        res=[]
        stack=[root]
        while stack!=[]:
            ans=[]
            q=[]
            for i in range(len(stack)):
                p=stack.pop(0)
                q.append(p.val)
                for child in p.children:
                    ans.append(child)
            res.append(q)
            stack=ans
        return res