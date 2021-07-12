t = int(input())
for i in range(t):
    n = int(input())
    k = int(input())
    s = input()
    if k == 1:
        print(1)
    else:
        for j in range(n-k):
            s[j:k].replace("1", "0")

        if all(x == "0" for x in s):
            print(1)
        else:
            print(0)
