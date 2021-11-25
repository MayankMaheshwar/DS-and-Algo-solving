a = list(s)
   for i in xrange(0, len(a), 2*k):
        a[i:i+k] = reversed(a[i:i+k])
    return "".join(a)
