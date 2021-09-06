class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        ans = [intervals[0]]
        if len(intervals) == 1:
            return ans

        cur = 0
        i = 1
        n = len(intervals)
        while i < n:

            if intervals[i][0] <= ans[cur][1]:
                temp = []
                if intervals[i][1] > ans[cur][1]:
                    temp = [ans[cur][0], intervals[i][1]]
                else:

                    temp = [ans[cur][0], ans[cur][1]]
                ans[cur] = temp

            else:
                ans.append(intervals[i])
                cur += 1
            i += 1
        return ans
