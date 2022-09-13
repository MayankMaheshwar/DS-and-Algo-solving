# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return head
        cur1=head
        cur2=head.next
        while cur2!=None:
            if cur2.next==None:
                return cur1.next
            cur2=cur2.next.next
            cur1=cur1.next
            
            
        return cur1