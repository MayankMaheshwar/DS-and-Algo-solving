nums = [1, 24, 42335, 43]
mx = max(nums)
print(nums.index(mx)) if all(i*2 <= mx for i in nums if i != mx) else -1
