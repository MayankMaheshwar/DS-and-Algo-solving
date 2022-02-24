# I will use a array and dictionary to add and searc respectively

# I use ordereddict to remove a num in constant time
from collections import OrderedDict


class DataStructure():
    def __init__(self, n):
        self.n = n
        self.arr = [-1]*n
        self.cur = 0
        self.front = 0
        self.index = 0
        self.dic = OrderedDict()

    def add(self, data):
        if self.front == self.n:
            self.front = 0
            cur = self.arr[self.front]
            del self.dic[cur]
            self.arr[front] = data
            self.dic[data] = self.index
            self.index += 1
            self.front += 1

        else:
            self.arr[front] = data
            self.front += 1

    def search(self, data):
        # corner case - If we have empty or partially filled array
        if self.cur == 0:
            return -1
        else:
            return self.binary_search(self.arr, 0, self.cur, data)

    def binary_search(self, nums, lo, hi, target):

        while lo <= hi:
            mid = (lo+hi) // 2
            if nums[mid] == target:
                return self.dic[nums[mid]]
            if nums[lo] <= nums[mid]:
                if target >= nums[lo] and target < nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                if target > nums[mid] and target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1

        return -1
