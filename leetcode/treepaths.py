# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []

        def helper(root, s):
            if root.left == None and root.right == None:
                s += str(root.val)
                self.res.append(s)
                return

            s += str(root.val)+"->"
            if root.left:

                helper(root.left, s)

            if root.right:
                helper(root.right, s)
        s = ""
        helper(root, s)
        return self.res
