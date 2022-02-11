def hn(n):
    t=0
    s=list(str(n))
    for i in s:
        t=t+(int(i)**2)
    if len(str(t))==1 and t==1:
        return True
    elif len(str(t))==1 and t!=1:
        return False    
    else:
        return hn(t)    
a=int(input())






