tc=int(input())
for i in range(tc):
    a=int(input())
    b=list(map(int,input().split()))
    count=0

    while not all(x==0 for x in b):
            if all(t%2==0 for t in b):
                    b=[e//2 for e in b]
                    count+=1
                    print(b)

            else:
                    for f in b:
                            if f%2!=0:
                                    f=f-1
                                    count+=1
                                    print(count)
                    print(b)

    print(count)
