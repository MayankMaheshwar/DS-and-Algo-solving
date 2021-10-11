# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def height(self, root, h):
        if root == None:
            return 0
        lh = self.height(root.left, self.h)
        rh = self.height(root.right, self.h)
        self.h = max(self.h, lh+rh)
        return max(lh, rh)+1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.h = 0
        self.height(root, self.h)
        return self.h


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.ans = 1

        def depth(node):
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
