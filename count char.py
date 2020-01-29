a=str(input())
a=a.replace(" ","")
b=list(a)
d={}
for i in b:
    x=b.count(i)
    d[i]=x

for key,value in d.items():
    print(key,'=',value)    



    


    

           
    


    


