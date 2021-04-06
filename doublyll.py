class DLL:
    def __init__(self, nxt=None, prv=None, val):
        self.nxt = None
        self.prv = None
        self.val = val

    def insert(self, node):
        if self.nxt == None:
            self.nxt = node.prv
            node.prv = self.nxt
        else:
            self.nxt = insert(node)


if __name__ == '__main__':
    dll1 = None
    l = [1, 23, 452, 3, 2, 0, "awwr"]
    for i in l:
        if dll1:
            newdll = DLL(i)
            dll1.insert(newdll)
        else:
            dll1 = DLL(i)

    print(dll1)
