# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left_pre = dummy
        curr_node = head

        for _ in range(left - 1):
            left_pre = left_pre.next
            curr_node = curr_node.next

        pre_node = None
        for _ in range(right - left + 1):
            next_node = curr_node.next
            curr_node.next = pre_node
            pre_node = curr_node
            curr_node = next_node

        left_pre.next.next = curr_node
        left_pre.next = pre_node

        return dummy.next
