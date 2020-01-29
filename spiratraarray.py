a=int(input())
t=0
for i in range(1,a+1):
    if len(str(i))==1:
        t=t+i
    else:
        s=list(str(i))
        for j in s:
            t=t+int(j)   
print(t)

