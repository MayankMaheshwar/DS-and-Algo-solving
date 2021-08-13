# Definition for binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


"Recursive"


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []

        def inorderTraversalHelper(root):
            if not root:
                return None
            inorderTraversalHelper(root.left)
            output.append(root.val)
            inorderTraversalHelper(root.right)
        inorderTraversalHelper(root)
        return output
