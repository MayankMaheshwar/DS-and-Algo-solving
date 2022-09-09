class Solution:
    def numberOfWeakCharacters(self, p: List[List[int]]) -> int:
        weakCharacters = 0
        maxDefense = 0
        p.sort(key = lambda x: (-x[0], x[1]))
        for _, defense in p:
            if defense < maxDefense: weakCharacters += 1
            else: maxDefense = defense
        return weakCharacters