A
A > B - [A, B]
A > D
A > B > C
D > B
E > P > Q

head -> {A, D, E}


{} -> {A: {}, }

A: {}


class Trie:
    def __init__(self):
        trie = {}


class Node:
    def __init__(self, name, trie):
        hash = name: {}

    def append(self, trie, products):
        level = trie
        i = 0
        while products[i] in level:
            level = level[products[i]]   A: {B: {}, D: {}}
            i += 1
        level[products[i]]

    def count(self, name, trie):
        c = 0
        level = trie
        while name not in level:
            c += 1
