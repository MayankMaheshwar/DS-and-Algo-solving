"""
We are given two arrays, entries and exits which denotes entry and exit times of n people coming to a hotel 
n = length of entries/exits array
entries = [4, 7, 9, 12]
exits = [8, 13, 11, 14]

We need to find minimum number of room hotel should have to accommodate all guests."""


def min_room(entries, exits):
    n = len(exits)
    exits.sort()
    ans = 0

    cur_entry = 0
    cur_exit = 0
    cur_room = 0
    while cur_entry < n:
        if entries[cur_entry] < exits[cur_exit]:
            cur_room += 1
            cur_entry += 1
        else:
            cur_room -= 1
            cur_exit += 1

        ans = max(cur_room, ans)

    return ans


entries = [4, 7, 9, 12]
exits = [8, 13, 11, 14]
print(min_room(entries, exits))
