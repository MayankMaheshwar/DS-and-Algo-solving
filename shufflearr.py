import random

def ra(arr,n):
    for i in range(0,n-1):
        j=random.randint(i+1,n)
        arr[i],arr[j]=arr[j],arr[i]
    return arr    
arr=[2,3,4,56,9]

print(ra(arr,len(arr)))


