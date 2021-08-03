    """
    You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.
    """



class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dic={}
        n=len(words)
        for word in words:
            for char in word:
                if char not in dic:
                    dic[char]=1
                else:
                    dic[char]+=1
        for char, value in dic.items():
            
            if value%n!=0:
                return False
        return True
                
            
        