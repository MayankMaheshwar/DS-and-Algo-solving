l=list(map(int,input().split()))
l.sort()
odd=[]
even=[]
sortoe=[]
for i in l:
    if i%2!=0:

            odd.append(i)
    else:
            even.append(i)
print(odd)
print(even)

for j in range(len(even)):
        sortoe.append(odd[j])
        sortoe.append(even[j])

if len(odd)>len(even):

        for k in range(len(even),len(odd)):
                sortoe.append(odd[k])
else:

        for g in range(len(odd),len(even)):
                sortoe.append(even[g])
        
print(sortoe)


