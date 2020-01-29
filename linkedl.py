class node:
    def __init__(self, data):
        self.data=data
        self.next=None

class ll:
    def __init__(self,head):
        self.head=None

    def insert_at_head(self,data):
        self.head=node(self,data)

    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    
            
