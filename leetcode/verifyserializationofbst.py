class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        p = preorder.split(',')

        # initially we have one empty slot to put the root in it
        slot = 1
        for node in p:

            # no empty slot to put the current node
            if slot == 0:
                return False

            # a null node?
            if node == '#':
                # ocuppy slot
                slot -= 1
            else:
                # create new slot
                slot += 1

        # we don't allow empty slots at the end
        return slot == 0
