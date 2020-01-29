t=int(input())
for i in range(t):
    z=int(input())
    a=list(map(int,input().split()))
    b=set(a)
    c={}
    for i in b:
        c[i]=a.count(i)     

    w=sorted(c,key=c.get,reverse=True)
    
    for i in w:
        for j in range(a.count(i)):
            print(i,end=" ")
    print()    
    
    
    
        
    