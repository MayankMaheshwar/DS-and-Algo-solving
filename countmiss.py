l=list(map(int,input().split()))
l.sort()
arr=[0]*len(l)
for i in range(len(l)):
    arr[l[i]]=1
    

