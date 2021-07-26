
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i in nums:
            if i not in a:
                a.add(i)
            else:

                return True
        return False
