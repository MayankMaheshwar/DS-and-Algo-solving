# Node Class
class Node:
    # Default Constructor
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    # A utility function to insert a new node with given key in BST
    def insert(self, val):

        # If the tree is empty, return a new node

        # Otherwise, recur down the tree
        if self == None:

            return Node(val)
        if val < self.key:

            self = self.left
            self.left = self.insert(val)

        else:
            self = self.right
            self.right = self.insert(val)


# BST Class
class binarySearchTree:
    def __init__(self, key):
        self.root = Node(key)

    def insert(self, key):
        self.root.insert(key)

# A utility function to do inorder tree traversal


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

# Let's create the above Binary Search Tree


BST = binarySearchTree(6)

BST.insert(3)
BST.insert(9)
BST.insert(1)
BST.insert(5)
BST.insert(7)
BST.insert(11)

# Print inoder traversal of the BST
inorder(BST.root)
