str = 'abcdghabcegfgahgzeg'
substr = 'ageg'

ans = 'ageg'

dic = {}
i = 0
j = 0
while ans != substr:
    while substr[j] != str[i]:
        i += 1
    if str[i] in ans and ans[-1] != str[i]:
        ans = ''
    else:
        ans += str[i]
        dic[str[i]] = i
    j += 1
print(ans)
print(dic)
