# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(-1)
        large = ListNode(-1)
        head_small = small
        head_large = large

        while head:
            if head.val<x:
                head_small.next = head
                head_small = head_small.next
            else:
                head_large.next = head
                head_large  = head_large.next
            head = head.next
        
        head_small.next = large.next
        head_large.next = None
        return small.next
