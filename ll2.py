class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

    def gd(self):
        return self.data

    def gn(self):
        return self.next    


    def sd(self): 
        self.data=data

    def sn(self):
        self.next=next

# getting address same of objects interlinked
a=node(0)
print(a)
b=node(1)
b=node(1,a)
print(b.gn())
count=0
# getting no. of elements in linked list and print each node's data
while b:
    count+=1
    print(b.data)
    b=b.next
print("Count=",count)


#Maintain a class for seperate linked list

class list():
    
    self.head=None

