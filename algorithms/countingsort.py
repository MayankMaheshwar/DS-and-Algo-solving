arr = [1,2,2,1,3,3,3,1,5]
max = max(arr)
countArr = [0] * (max+1)

for i in range(len(arr)):
    countArr[arr[i]]+=1
print(countArr)    
for i in range(1,len(countArr)):
    countArr[i]+= countArr[i-1]
print(countArr)
sortedArray=[0]*len(arr)
for i in range(len(arr)-1,-1,-1):
    countArr[arr[i]]-=1    
    sortedArray[countArr[arr[i]]]=arr[i]
print(sortedArray)    
    
