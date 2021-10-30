class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        i = r0
        j = c0
        coordinates = [[r0, c0]]
        step_size = 1
        sign = 1
        while len(coordinates) < R*C:
            for _ in range(step_size):
                j += sign
                if i < R and j < C and i >= 0 and j >= 0:
                    coordinates.append([i, j])
            
            for _ in range(step_size):
                i += sign
                if i < R and j < C and i >= 0 and j >= 0:
                    coordinates.append([i, j])
            
            step_size += 1
            sign *= -1
        return coordinates