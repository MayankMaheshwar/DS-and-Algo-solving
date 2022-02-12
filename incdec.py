class Solution:
    def sortString(self, s: str) -> str:
        cnt, ans, asc = collections.Counter(s), [], True
        # if Counter not empty.
        while cnt:
            # traverse keys in ascending/descending order.
            for c in sorted(cnt) if asc else reversed(sorted(cnt)):
                # append the key.
                ans.append(c)
                # decrease the count.
                cnt[c] -= 1
                # if the count reaches to 0.
                if cnt[c] == 0:
                    # remove the key from the Counter.
                    del cnt[c]
            # change the direction, same as asc ^= True.
            asc = not asc
        return ''.join(ans)
