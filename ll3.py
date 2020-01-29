class node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=node(4)
b=node(5)
c=node(6)
d=node(7)
e=node(8)
a.next=b
b.next=c
c.next=d
d.next=e
count=0
while a:
    print(a.data,end=" ")
    count+=1
    a=a.next
print()   
print(count)
z=count//2+1
print(z)
y=0
while a!=None:
    y+=1
    if y==z:
        print(a.data)
        
    a=a.next
