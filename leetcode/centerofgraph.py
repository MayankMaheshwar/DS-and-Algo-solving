class Solution:
    def findCenter(self, edges):
        a = edges[0][0]
        b = edges[0][1]
        if b in edges[1]:
            return b
        else:
            return a
