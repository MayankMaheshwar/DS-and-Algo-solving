from collections import defaultdict
dic = defaultdict(list)

string = """John is at a postn to find more."""

for str in string:
    st = sorted(str)
    if st in dic:
        dic[st].append(str)
    else:
        dic[st] = [str]


for key, value in dic.items():
    print(",".join(value))
