from collections import defaultdict
dic=defaultdict(list)

string="""John is at a post, where they make pots. Making the pots will
stop in the future. Oh dear, what will happen to them when it
happens. This can happen only in Rome. Read on to find more."""

for str in string:
    st=sorted(str)
    if st in dic:
        dic[st].append(str)
    else:
        dic[st]=[str]


for key, value in dic.items():
    print(",".join(value))