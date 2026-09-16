# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None

        slow, fast = head, head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        half = slow.next
        slow.next = None

        prev = None
        curr = half

        curr = half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        half = prev
        
        first = head
        while half:
            tmp1 = first.next
            tmp2 = half.next
            
            first.next = half
            half.next = tmp1
            
            first = tmp1
            half = tmp2


