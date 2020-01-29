w=[]
for i in range(int(input())):
    w.extend(input().split())
   
for i in range(int(input())):
    s=input()
    s1=""
    if s[len(s)-3:]=="our":
        s1=s[:len(s)-3]+"or"
    else:
     
        s1=s[:len(s)-2]+"our"
     
    
    print(w.count(s1)+w.count(s))    

        

    



