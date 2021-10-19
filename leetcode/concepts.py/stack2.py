class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        for num in nums2:
            while stack != [] and num > stack[-1]:
                dic[stack.pop()] = num
            stack.append(num)

        for num in range(len(nums1)):
            if nums1[num] in dic.keys():
                nums1[num] = dic[nums1[num]]
            else:
                nums1[num] = -1

        return nums1
