
# 1st solution
from collections import defaultdict
dic=defaultdict(set)

string="""John is at a post, where they make pots. Making the pots will stop in the future. Oh dear, what will happen to them when it happens. This can happen only in Rome. Read on to find more."""

string=string.replace(".","")
string=string.replace(",","")
string=list(string.split(" "))

for str in string:
    st="".join(sorted(str.upper()))
    
    if st not in dic:
        dic[st]={str}
    else:
        dic[st].add(str)

for key,value in dic.items():
    if len(value)>1:
        
        print(list(sorted(value)))



# 4th solution
string="co?3d5er45,3"
negative=True if string[0]=="-" else False
string=[str for str in string if str.isdigit()]
if len(string)<=3:
    print(-1)
else:
    string[1],string[0]=string[0],string[1]
    string[-1],string[-2]=string[-2],string[-1]
    print("".join(string))


# 3rd solution
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