s="ab*c+d*e/"
stack = []
op=('+','-','*','/')
for i in range(len(s)):
    if s[i] not in op:
        stack.append(s[i])
    else:
        print(stack.pop(0))
        print(s[i])
   
print(stack.pop())

