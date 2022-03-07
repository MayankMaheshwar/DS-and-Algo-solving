"""
Python interview question

Sort 0's and 1's left to right
0's on the left and 1's on the right

- Time complexity O(n)
- Space complexity O(1) - It should be in place, cannot create a new array or create a new variable
- Array can only be traversed once
- Cannot use the length function
"""

list = [0, 1, 1, 1, 0, 0, 1, 0, 1]

left = 0
right = 1

while True:
    try:
        if list[left] != 0 and list[right] != 1:
            list[left], list[right] = list[right], list[left]
            left += 1
            right += 1

        elif list[left] != 0 and list[right] == 1:
            right += 1

        else:
            left += 1

    except:
        break


print(list)
