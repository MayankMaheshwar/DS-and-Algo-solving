class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class bt:
    def __init__(self):
        self.root=None

    
    def il(self,data):
        t=bt(data)
        if self.left==None:
            self.left=t
        else:
            t.left=self.left
            self.left=t

    def ir(self,data):
        t=bt(data)
        if self.right==None:
            self.right=t
        else:
            t.right=self.right
            self.right=t 

    def iot(self):
        if root:
            iot(root.left)
            print(root.data)
            iot(root.right)

a=bt()
a.il(6)
a.il(7)
a.ir(3)
a.ir(4)
a.iot()



                 


