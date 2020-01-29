for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in range(0,n-1):
        if l[i]%2==0:
            c+=1
            for j in range(i+1,n):
                if l[i]+l[j]%2==0:
                    c+=1
    if l[-1]%2==0:
        print(c+1)
    else:
        print(c)
        