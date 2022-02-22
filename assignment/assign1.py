"""
1. Given a string of size n ( may contain duplicate characters), generate sub sequence of
size k (should contain only unique characters) and print them in lexicographic order.
Example:
1. str1=“kabccr” size(n) = 6, k=3
Solution: subsequences: abc, abk, abr, acb, ack,
acr,akb,akc,akr,arb,arc,arb,arc,ark,bac,bak,bar,bca,bck,bcr……………..
"""


from itertools import permutations
string = "kabccr"
str_list = list(set(string))

list_of_perms = list(permutations(str_list, 3))

join_strings = []
for si in list_of_perms:
    join_strings.append("".join(si))


result = sorted(join_strings, key=str.lower)
print(result)
