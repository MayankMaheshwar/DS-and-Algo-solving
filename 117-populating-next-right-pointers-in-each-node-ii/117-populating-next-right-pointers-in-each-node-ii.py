"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None: return None

        q = deque([root])
        while q:
            prev = None
            for _ in range(len(q)):
                curr = q.popleft()
                if _ == len(q)-1:
                    curr.next=None
                if prev==None:
                    prev=curr
                else:
                    prev.next=curr
                    prev=curr

                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)
        return root