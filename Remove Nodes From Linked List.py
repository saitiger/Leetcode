class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function to reverse the linked list
        def reverse_list(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        reversed_head = reverse_list(head)
        
        dummy = ListNode(0)  
        dummy.next = reversed_head
        current = reversed_head
        max_value = float('-inf')
        
        while current and current.next:
            max_value = max(max_value, current.val)
            if current.next.val < max_value:
                current.next = current.next.next
            else:
                current = current.next
        
        return reverse_list(dummy.next)
