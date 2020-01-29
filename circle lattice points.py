import math
def lattice(r):
    if r<=0:
        return r
        
    else:
        result=4
        for x in range(1,r):
            ysq=r**2 - x**2
            y=int(math.sqrt(ysq))
            if y**2==ysq:
                result+=4
        return result        
        


for i in range(int(input())):
    n=int(input())
    print(lattice(n))