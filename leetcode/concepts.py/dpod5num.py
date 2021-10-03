
def solve(A, B, C, D):
    prime1 = A
    prime2 = B
    prime3 = C
    count = 0
    ans = []
    i, j, k = 0, 0, 0
    while count != D:
        temp = min(prime1, prime2, prime3)
        ans.append(temp)
        count += 1
        if temp == prime1:
            prime1 = A*ans[i]
            i += 1
        if temp == prime2:
            prime2 = B*ans[j]
            j += 1
        if temp == prime3:
            prime3 = C*ans[k]
            k += 1
    return ans


print(solve(2, 11, 5, 4))
