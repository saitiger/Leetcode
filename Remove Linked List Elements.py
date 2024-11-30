# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Iterate through the list
        while current and current.next:
            if current.next.val == val:
                # Remove the node with the matching value
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        # Return the new head (dummy.next skips the dummy node)
        return dummy.next
