class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        a = sum(A)
        b = sum(B)
        avg = (a+b)//2
        adiff = a-avg
        setb = set(B)
        for elemneta in A:
            if elemneta-adiff in setb:
                return [elemneta, elemneta-adiff]
