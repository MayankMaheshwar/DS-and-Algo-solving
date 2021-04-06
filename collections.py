from collections import  Counter, OrderedDict, namedtuple
import collections
# number appearing frequently..if two return lowest

arr=[34,234,23,34,23,23,1,2,3,34]
c=sorted(OrderedDict(Counter(arr)).items(),key=lambda x:x[1],reverse=True)

# namedtuple


family=namedtuple('famil','h w g')
mayank=family(h=23,w=45,g=32)
print(mayank._asdict())


# defaultdict

lis=[3,42,3,2,2,3]
d=collections.defaultdict(list)
for i in lis:
    d[i].append(i)
print(d)    

