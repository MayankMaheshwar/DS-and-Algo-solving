# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        total = []
        curSum = []

        def h(root, ts, cs, t):
            if root:

                if not root.left and not root.right and sum(cs)+root.val == ts:
                    t.append(cs+[root.val])

                h(root.left, ts, cs+[root.val], t)
                h(root.right, ts, cs+[root.val], t)

        h(root, targetSum, curSum, total)
        return total
