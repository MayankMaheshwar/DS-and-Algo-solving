class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        ans=""
        for x in words:
            ans+=x
            if ans==s:
                return True
        return False