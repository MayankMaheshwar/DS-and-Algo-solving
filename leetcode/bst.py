# implementation
from treelib import Node, Tree


class bst:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, data):
        cur = self.val
        if cur > data:
            cur.right = bst(data)
        else:
            cur.left = bst(data)


tree = bst(5)
T = Tree(tree)
print(T.show())
