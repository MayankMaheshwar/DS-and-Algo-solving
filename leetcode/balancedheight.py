# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        self.flag = True

        def rec(root):
            if root == None:
                return 0
            l = rec(root.left)
            r = rec(root.right)
            if abs(l-r) > 1:
                self.flag = False
            return max(l, r)+1
        rec(root)
        return self.flag
