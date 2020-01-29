def c(n,l):
    l=list(filter(lambda x:x<=n,l))
    count=0
    st=[]
    for i in l:
        
        equal=0
        while equal<=n:
            equal+=i
            a=n-equal
            s1=a+i
            
            if a in l and s1 not in st:
                
                st.append(s1)
                
                count+=1
                
    return count  
            
            
    
    
for i in range(int(input())):
    n=int(input())
    l=[3,5,10]
    print(c(n,l))
    
    