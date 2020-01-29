tc=int(input())
for i in range(tc):
    a=int(input())
    b=list(map(int,input().split()))
    water=0
    
    
    for j in range(0,a-1):
        if b[j]>b[j+1]:
           
            for k in range(j+1,a):
                
                
                count=0
                ind=0
                if b[k]>=b[j]:
                    ind=k
                    count+=1
                if count==1:
                    
                    for l in range(j+1,k):
                        water+=b[j]-b[l]
                        
                        print(water)
        j+=ind      
    
                    
                
    
            
            