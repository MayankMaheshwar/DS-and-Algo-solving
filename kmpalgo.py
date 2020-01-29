for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    
    for i in range(1,n,2):
        if l[i]<l[i-1]:
            l[i],l[i-1]=l[i-1],l[i]
        if i+1<n:
            if l[i]<l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
    print(*l)        