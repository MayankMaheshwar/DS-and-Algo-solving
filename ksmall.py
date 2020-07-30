
tc=int(input())
for t in range(tc):
    size,total=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for g in range(len(l)):
        c=c+l[g]
        for k in range(1,len(l)):
            c=c+l[k]
            if c==total:
                print(g,k)
               