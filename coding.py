tc = int(input())
for i in range(tc):
    dict = {}
    entries = int(input())
    for i in range(entries):
        name,tweetId = map(str,input().split())
        if name not in dict:
            dict[name] = 1
        else:
            dict[name] += 1
    dict = sorted(dict.items(),key=lambda x:x[1],reverse=True ) 

    another_dict = {}
    max = dict[0][1]
    for key, value in dict:
        if value < max:
            break
        another_dict[key] = value

    for key in sorted(another_dict.keys()):
        print(key, another_dict[key])
