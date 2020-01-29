class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class llk:
    def __init__(self):
        self.head=None

    def push(self,data):
        
        new=node(data)
        new.next=self.head
        self.head=new

    def r(self,val):
        cur=self.head
        temp=cur.next
        while temp:
            if cur.data==val:
                
                cur
                break
            cur=cur.next
            temp=temp.next                   

    def p(self):
        cur=self.head
        while cur!=None:
            print(cur.data)
            cur=cur.next

a=llk()
a.push(2)
a.push(3)
a.push(7)
a.push(8)
a.r(8)
a.p()
