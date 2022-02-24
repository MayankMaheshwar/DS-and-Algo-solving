# I will use a array and dictionary to add and search respectively

# Also binary search will return the last index of duplicate values

# I use ordereddict to remove a num in constant time
from collections import OrderedDict


class DataStructure():
    def __init__(self, n):
        self.n = n   # last n numbers
        self.arr = [-1]*n  # initial array
        self.front = 0  # used for rotating index and assign the new values
        self.index = 0  # will use for increment the indices of stream of numbers
        self.dic = OrderedDict()  # keep track of indices of nums

    def add(self, data):
        if self.front == self.n:  # time to rotate the array if it's full
            self.front = 0        # again main front to 0
            cur_data = self.arr[self.front]  # assign the new value
            del self.dic[cur_data]              # delete the prev value
            self.arr[self.front] = data    # assign the new value
            self.dic[data] = self.index   # store the new value with cur index
            self.index += 1                 # increment the index
            self.front += 1                 # increment the index

        else:
            self.arr[self.front] = data
            self.dic[data] = self.index
            self.index += 1
            self.front += 1

    def search(self, data):
        # corner case - If we have empty or partially filled array

        return self.binary_search(self.arr, 0, self.front-1, data)

    def binary_search(self, nums, l, r, target):

        if not nums:
            return -1

        while l < r:
            mid = (l + r)//2
            if nums[mid] == target:
                return self.dic[nums[mid]]
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r -= 1
        return self.dic[nums[l]] if nums[l] == target else -1


obj = DataStructure(3)
obj.add(1)
obj.add(1)
obj.add(3)


print(obj.search(1))

obj.add(4)

print(obj.search(4))
