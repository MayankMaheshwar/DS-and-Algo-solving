def generate(arr):
            if not arr:
                return [None]
            ans = []
            for i in range(len(arr)):
                lefts, rights = generate(arr[:i]), generate(arr[i+1:])
                for l in lefts:
                    for r in rights:
                        root, root.left, root.right = TreeNode(arr[i]), l, r
                        ans.append(root)
            return ans

        return(generate(list(range(1,n+1)))) if n else []
