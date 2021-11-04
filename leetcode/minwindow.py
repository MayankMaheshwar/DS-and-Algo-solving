from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_cnt = collections.Counter(t)
        
        i, found = 0, 0
        min_win = ""
        for j in range(len(s)):
            if target_cnt[s[j]]>0:found += 1
            print(target_cnt)
            target_cnt[s[j]] -=1
            while found==len(t):
                #print(i, j, target_cnt)
                if not min_win or j-i+1<len(min_win):
                    min_win = s[i:j+1]
                target_cnt[s[i]]+=1
                
                if target_cnt[s[i]]>0:found -=1
                i+=1
        return min_win
                
        