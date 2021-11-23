# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if len(res) > 1:
                return

            if node.left:
                findNode(node.left, res)

            res[0] -= 1
            if res[0] == 0:
                res.append(node.val)
                return
            
            if node.right:
                findNode(node.right, res)
                
        res = [k]
        findNode(root, res)
        return res[1]
        
