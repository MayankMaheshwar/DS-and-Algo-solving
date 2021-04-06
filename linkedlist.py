class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert(self, node):
        if not self.next:
            self.next = node

        else:
            self.next.insert(node)

    def __str__(self):
        if self.next:
            return '%s -> %s' % (self.value, str(self.next))
        else:
            return ' %s ' % self.value


if __name__ == "__main__":
    items = ['a', 'b', 'c', "d", 2, 'e']
    ll = None
    for item in items:
        if ll:
            next_ll = LinkedList(item)
            ll.insert(next_ll)

        else:
            ll = LinkedList(item)
    print('[ %s ]' % ll)
