def solution(N):
    # write your code in Python 3.6
    binary = bin(N)[2:]

    print(bin(N), binary)
    mx = 0
    cur = 0
    for bi in range(1, len(binary)):
        if binary[bi-1] == '1' and binary[bi] == '0':
            cur = 1
            print(cur, mx, '1')
        elif binary[bi-1] == '0' and binary[bi] == '0':
            cur += 1
            print(cur, mx, '2')
        elif binary[bi-1] == '0' and binary[bi] == '1':
            print(cur, mx, '3')
            if cur > mx:
                mx = cur

    return mx


print(solution(1041))
