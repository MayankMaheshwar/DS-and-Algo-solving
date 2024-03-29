ans = 0
q = deque()

 q.append((root, -inf))
  '''perform bfs  with track of maxval till perant node'''

   while q:
        node, maxval = q.popleft()
        '''if curr node has max or eqvalue till current max'''
        if node.val >= maxval:
            ans += 1

        if node.left:  # new max update
            q.append((node.left, max(maxval, node.val)))

        if node.right:
            q.append((node.right, max(maxval, node.val)))

    return ans
