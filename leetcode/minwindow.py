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
                
def found_target(target_len):
    return target_len == 0

class Solution(object):
    def minWindow(self, search_string, target):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target_letter_counts = collections.Counter(target)
        start = 0
        end = 0
        min_window = ""
        target_len = len(target)        
        
        for end in range(len(search_string)):
			# If we see a target letter, decrease the total target letter count
			if target_letter_counts[search_string[end]] > 0:
                target_len -= 1

            # Decrease the letter count for the current letter
			# If the letter is not a target letter, the count just becomes -ve
			target_letter_counts[search_string[end]] -= 1
            
			# If all letters in the target are found:
            while found_target(target_len):
                window_len = end - start + 1
                if not min_window or window_len < len(min_window):
					# Note the new minimum window
                    min_window = search_string[start : end + 1]
                    
				# Increase the letter count of the current letter
                target_letter_counts[search_string[start]] += 1
                
				# If all target letters have been seen and now, a target letter is seen with count > 0
				# Increase the target length to be found. This will break out of the loop
                if target_letter_counts[search_string[start]] > 0:
                    target_len += 1
                    
                start+=1
                
        return min_window
        