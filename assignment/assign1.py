"""
1. Given a string of size n ( may contain duplicate characters), generate sub sequence of
size k (should contain only unique characters) and print them in lexicographic order.
Example:
1. str1=“kabccr” size(n) = 6, k=3
Solution: subsequences: abc, abk, abr, acb, ack,
acr,akb,akc,akr,arb,arc,arb,arc,ark,bac,bak,bar,bca,bck,bcr……………..
"""


str = "kabccr"
s = "".join(sorted(str))

k = 3

ans = []
n = len(s)


def size_k_subsequence(s, cur_pos, dic, cur_str):

    if cur_pos == n:
        return

    if len(cur_str) == k:
        print(cur_str)
        return

    if s[cur_pos] not in dic:
        dic[cur_str] = True

    if s[cur_pos] in dic:
        cur_pos += 1

    for i in range(cur_pos, n):

        size_k_subsequence(s[i:], cur_pos, dic, cur_str+s[cur_pos])

    size_k_subsequence(s, cur_pos+1, dic, cur_str)


size_k_subsequence(s, 0, {}, "")
