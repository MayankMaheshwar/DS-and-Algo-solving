class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        mask = functools.reduce(lambda x, y: x | 1 << ord(y) - ord('a'), brokenLetters, 0)
        return sum(1 for word in text.split() if all(((1 << ord(c) - ord('a')) & mask) == 0 for c in word))