class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        p1 = None
        p2 = None
        
        temp = head
        while temp:
            if p2 is not None:
                p2 = p2.next
                
            k -= 1
            if k == 0:
                p1 = temp
                p2 = head
                
            temp = temp.next
        
        p1.val, p2.val = p2.val, p1.val
        return head
