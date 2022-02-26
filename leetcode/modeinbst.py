
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = collections.Counter()

        def dfs(node):
            if node:
                count[node.val] += 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        max_ct = max(count.values())
        return [k for k, v in count.items() if v == max_ct]
