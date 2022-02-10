arr = [434, 12, 34, 12, 43, 5354, 3221, 42, 44, 2, 4, 16]
no = 8

flag = False
for num in arr:
    if num % no == 0:
        flag = True

if flag == False:
    sum_of_arr = sum(arr)
    if sum_of_arr % no == 0:
        flag = True

print(flag)
print("yes")
