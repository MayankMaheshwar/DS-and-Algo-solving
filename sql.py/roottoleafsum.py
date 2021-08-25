# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.arr = []
        cur = ''

        def help(root, cur):
            if root:
                if not root.left and not root.right:
                    self.arr.append(cur+str(root.val))
                    return
                cur += str(root.val)
                help(root.left, cur)

                help(root.right, cur)

        help(root, cur)
        ans = 0
        for i in self.arr:
            ans += int(i, 2)
        return ans
