
n1,n2=map(int, input().split())
f1=[1,n1]
f2=[1,n2]

for i in range(2,int(n1**0.5)+1):
    if n1%i==0:
        f1.append(i)
        f1.append(int(n1/i))
print(f1)  
print(int(n2**0.5)+1)
for i in range(2,int(n2**0.5)+1):
    if n2%i==0:
        f2.append(i)
        f2.append(int(n2/i))
print(f2)       
    #print(f1,f2)
print(len(set(f1)&set(f2)))
    

