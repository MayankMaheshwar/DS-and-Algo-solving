l=list(map(int,input().split()))
mtn,m=0,0
if all(x>0 for x in l):
    print(sum(l))
elif all(x<=0 for x in l):
    print(max(l))
else:
    for w in l:
        mtn=mtn+w
        
        if mtn<0:
            mtn=0
        
        else:
            m=mtn    
    print(m)    
            