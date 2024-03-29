# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow=head
        fast=head.next
        while fast!=None:
            slow=slow.next
            if not fast.next or not fast.next.next:
                return False
            fast=fast.next.next
            if slow==fast:
                return True
        return False