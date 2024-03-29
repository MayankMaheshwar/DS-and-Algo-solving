stack = []

while True:
    while root:
        stack.append(root)
        root = root.left
    root = stack.pop()
    k -= 1
    if not k:
        print(root.val)
    root = root.right


class Solution:
    def kthSmallest(self, root, k):

        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]
