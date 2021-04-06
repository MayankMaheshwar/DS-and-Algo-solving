def insert(n,stack):
    if stack==[]:
        stack.append(n)
    else:    
        curlar=stack.pop()
        if curlar>n:
            stack.append(n)
            stack.append(curlar)
        else:
            stack.append(curlar)
            stack.append(n)        
    return stack


def lar(stack):
    return stack.pop()
    


stack=[]
for i in range(5):
    n=int(input())
    stack=insert(n,stack)
    

print(stack)

