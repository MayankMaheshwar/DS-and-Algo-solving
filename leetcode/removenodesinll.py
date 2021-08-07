# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None
        prev = None
        cur = head
        while cur != None:
            if cur.val == val:
                if cur == head:
                    prev = head = head.next
                else:
                    prev.next = cur.next
                    cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return head
