from itertools import groupby


def solution(S):
    # write your code in Python 3.6

    if len(S) == 1:
        return 0

    mx = -2**32

    group = groupby(S)
    for k, v in group:
        mx = max(mx, len(list(v)))

    print(group, "yes")

    for j, l in group:
        print(j, l)

    print(group)
    return 0


print(solution("babaa"))
