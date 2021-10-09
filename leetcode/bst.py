class bst:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, data):
        cur = self.val
        if cur==data:
            return
        if cur > data:
            if not cur:
                cur.right = bst(data)
            else:
                cur=cur.right
        else:
            
            
            
        else:
            cur.left = bst(data)


tree = bst(5)

 