class cq():
    def __init__(self):
        self.q = [None]*10
        self.front=-1
        self.rear=-1

        

    def eq(self, data):
        if rear==len(self.q)-1 and front==0:
            print("full")

        else:
            if front==-1 and rear==-1:
                self.q.append(data)

                front+=1
                rear+=1
            else:    
                self.q.append(data)
                

    def dq(self):
        if front==-1 and rear==-1:
            print("empty")
        
        self.q.pop(0)


    def peek(self):
        if front==-1 and rear==-1:
            print("empty")
        else:
            print(self.q[front])


