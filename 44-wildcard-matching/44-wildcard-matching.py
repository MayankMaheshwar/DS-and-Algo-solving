class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dfs(i, j):
            if j == len(p):  # Reach full pattern
                return i == len(s)

            if i < len(s) and (s[i] == p[j] or p[j] == '?'):  # Match Single character
                if dfs(i + 1, j + 1): 
                    return True
            elif p[j] == '*':
                if dfs(i, j + 1):  # Match empty character
                    return True
                if i < len(s) and dfs(i + 1, j):  # Match one or more character
                    return True
            return False

        return dfs(0, 0)
