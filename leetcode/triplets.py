class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        threshold1 = threshold2 = float("inf")
        for num in nums:
            # lower threshold1
            if num <= threshold1:
                threshold1 = num
            # lower threshold2
            elif num <= threshold2:
                threshold2 = num
            # if greater than both thresholds (note equal doesn't count)
            else:
                return True
        return False