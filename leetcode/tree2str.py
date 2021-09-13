# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: Optional[TreeNode]) -> str:
        ans = ""

        def helper(t, ans):

            if t is None:
                return ""

            ans = str(t.val)

            if t.left:
                ans += "(" + self.tree2str(t.left) + ")"

            if not t.left and t.right:
                ans += "()"

            if t.right:
                ans += "(" + self.tree2str(t.right) + ")"

            return ans
        return helper(t, ans)
