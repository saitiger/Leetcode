# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Using Stack  
def reverse_linked_list(head):
    temp = head  
    stack = []   
    while temp is not None:
        stack.append(temp.data) 
        temp = temp.next        
    temp = head  
    while temp is not None:
        temp.data = stack.pop()  
        temp = temp.next        
    return head  

# Without Stack 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
