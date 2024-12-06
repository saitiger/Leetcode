# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head
        while curr and curr.next:
            to_swap_1 = curr.next
            to_swap_2 = curr.val
            curr.val = to_swap_1.val
            to_swap_1.val = to_swap_2
            curr = curr.next.next
        return head
