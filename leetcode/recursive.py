dic = {'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y': 10}}, 'd': [1, 2, 3]}


ans = {}


def rec(cur, dic):
    if type(dic) != dict:
        ans[cur] = dic
        return
    for key, val in dic.items():
        if cur == "":
            rec(key, val)
        else:
            rec(cur+"_"+key, val)


cur = ''
rec(cur, dic)
print(ans)
