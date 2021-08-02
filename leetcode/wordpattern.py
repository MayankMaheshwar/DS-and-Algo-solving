"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        pattern_dict = {}

        if len(pattern) != len(words):
            return False

        for p, w in zip(pattern, words):
            if pattern_dict.get(p):
                if pattern_dict[p] != w:
                    return False
            else:
                if w in pattern_dict.values():
                    return False
                pattern_dict[p] = w

        return True
