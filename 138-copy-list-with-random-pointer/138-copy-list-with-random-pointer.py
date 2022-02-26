"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import collections
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        map_new = collections.defaultdict(lambda: Node(0,0,0))
        map_new[None] = None # if a node's next or random is None, their value will be None but not a new Node, doing so removes the if-else check in the while loop
        
        nd_old = head
        while nd_old:
            map_new[nd_old].val = nd_old.val
            map_new[nd_old].next = map_new[nd_old.next]
            map_new[nd_old].random = map_new[nd_old.random]
            nd_old = nd_old.next
            
        
        return map_new[head]
