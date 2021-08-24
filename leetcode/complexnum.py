class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        num1 = num1.split('+')
        
        num1[0], num1[1] = int(num1[0]), int(num1[1][:-1])
        print(num1)

        num2 = num2.split('+')
        num2[0], num2[1] = int(num2[0]), int(num2[1][:-1])
        print(num2)
        real = [str(num1[0]*num2[0]-num1[1]*num2[1])] 
        print(real)
        img = [str(num1[0]*num2[1] + num1[1]*num2[0]) + 'i']
        print(img)
        ans = real + img
        print(ans)
        return '+'.join(ans) 
        