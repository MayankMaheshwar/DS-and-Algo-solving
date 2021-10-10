class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class bst:
    def __init__(self):
        self.root = None

    def ir(self, data, node):
        if data < node.data:

            if node.left == None:
                node.left = Node(data)
            else:
                self.ir(data, node.left)

        else:
            if node.right == None:
                node.right = Node(data)
            else:
                self.ir(data, node.right)

    def i(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.ir(data, self.root)

    def gmin(self):
        if self.root:
            return self.getmin(self.root)

    def getmin(self, node):
        if node.left:
            return self.getmin(node.left)
        return node.data

    def gmax(self):
        print(self.node)

    def getmax(self, node):
        print(self.root)


a = bst()
a.i(10)
a.i(5)
a.i(15)
a.i(6)


print(a.gmin())
print(a.gmax())
