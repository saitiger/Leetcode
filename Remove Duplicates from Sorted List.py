# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head  # Start with the head of the list
        while current and current.next:  # Traverse until the end of the list
            if current.val == current.next.val:  # If duplicate is found
                current.next = current.next.next  # Skip the duplicate node
            else:
                current = current.next  # Move to the next node
        return head  # Return the modified list
