class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            # corner case
            return False

        sum_of_factor = 1

        for i in range(2, floor(num**0.5) + 1):

            if num % i == 0:

                if i == num // i:
                    # square root, should only add once
                    sum_of_factor += i

                else:
                    # add factor i and (num // i)
                    sum_of_factor += (i + num // i)

        return sum_of_factor == num
