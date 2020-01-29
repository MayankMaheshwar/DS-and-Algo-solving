from math import sqrt,ceil
def isPrime(p):
    a=True
    for k in range(2,int(ceil(sqrt(p)+1))):
        if p%k==0:
            a=False
    return(a)        
tc=int(input())
for i in range(tc):      
    num=int(input())
    for j in range(2,num):
        if isPrime(j) and isPrime(num-j):
            print(j,num-j)
            break
            
                 