def fibo(n):
    if n>=3:
        return fibo(n-2)+fibo(n-1)
    
    else:
        return 1    
    



n=int(input())

print(fibo(n))





