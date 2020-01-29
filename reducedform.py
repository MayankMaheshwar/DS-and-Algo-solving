n=int(input())
l=list(map(int,input().split(' ')))
a=sorted(l)


for i in l:
    for j in a:
        if i==j:
            print(a.index(j),end=" ")
    

   


