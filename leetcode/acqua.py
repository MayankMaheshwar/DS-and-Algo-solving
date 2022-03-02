def check_cousins(root, c1, c2):
    queue = [root]
    c1flag = False
    c2flag = False
    c1p = None
    c2p = None

    while queue != None:
        while cur_child != None:

        cur_child = []
        cur = queue.popleft()
        if cur == c1:
            c1flag = True
            c1p = cur
        if cur == c2:
            c2flag = True
            c2p = cur

        if cur.left:
            cur_child.append(cur.left)
        if cur.right:
            cur_child.append(cur.right)
        if c2flag and c1flag and c1p != c2p:
            return True

    return False
