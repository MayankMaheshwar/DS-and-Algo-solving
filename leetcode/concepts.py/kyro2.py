def checkBST(head):
    neg = -2**32
    pos = 2**32

    def helper(head, neg, pos):
        if head == None:
            return True
        if head < neg or head > pos:
            return False
        return helper(head.left, neg, head.val) and helper(head.right, head.val, pos)

    return helper(head, neg, pos)
