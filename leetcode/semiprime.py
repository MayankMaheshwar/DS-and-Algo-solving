class Solution:

    def run(self, number):
        #
        # Write your code below; return type and arguments should be according to the problem's requirements
        #
        def is_prime(n):
            if n == 2 or n == 3:
                return True
            if n < 2 or n % 2 == 0:
                return False
            if n < 9:
                return True
            if n % 3 == 0:
                return False
            r = int(n**0.5)
            f = 5
            while f <= r:
                if n % f == 0:
                    return False
                if n % (f+2) == 0:
                    return False
                f += 6
            return True
        for d1 in range(2, int(number**.5)+1):
            if number % d1 == 0:
                d2 = number / d1
                return is_prime(d1) and is_prime(d2)
        return False
