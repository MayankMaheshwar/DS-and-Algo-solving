string="abcdef"
output=""
countSeq=0
match=0
cur=0
for i in range(1,len(string)):



    curmatch=abs(ord(string[i-1])-ord(string[i]))
    
    if countSeq==0:
        match=curmatch
        countSeq+=1
        cur=i-1
    elif curmatch==match:
        countSeq+=1
        
    
    j=i
    
    while match==curmatch and countSeq>=3 and j<len(string):
        curmatch=abs(ord(string[j-1])-ord(string[j]))
        if curmatch==match:
            countSeq+=1
            match=curmatch
        
        j+=1
    
    if countSeq>=3:
        
        output+=string[cur]+'-'+string[j-1]+'$'+str(match)
        countSeq=0

    


print(output)