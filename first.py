s1="Hello"
s2="Hi"
s3="Good Morning"
n=0
if len(s1)>len(s2):
    n=len(s1)
else:
    n=len(s2)
for i in range(n):
    if i in ['a','e','i','o',u] and i in s1:
        s1.replace(s1[i],"/"")
    elif i not in ['a','e','i','o',u] and i in s2:
        s2.replace(s2[i],"/"")
print(s1)
print(s2)

