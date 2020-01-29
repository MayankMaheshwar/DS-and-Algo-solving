for i in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    s=0
    for j in range(0,a-1):
        
        c=b[j]
        s+=bin(c)[2:].zfill(32).count("1")
    print(s*2)































8
-1865008399 -524833575 -1162539990 -1003374718 -1677272376 -2046456104 -689632770 -688705725
