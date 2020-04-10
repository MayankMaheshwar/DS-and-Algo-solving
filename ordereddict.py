from collections import OrderedDict
dic=OrderedDict()
n=int(input())
for _ in range(n):
    name,space,price = input().rpartition(' ')
    
    
    if name not in dic:
        dic[name]=int(price)
    else:
        dic[name]+=int(price)

for k,v in dic.items():
    print(k,v)
