class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        prefix_sum = 0
        mp = {}
        
        dummy = ListNode(0,head)
        mp[0] = dummy
        
        current = head
        
        while current:
            prefix_sum += current.val
            
            if prefix_sum in mp:
                # Find the previous node where the same prefix sum occurred
                P = mp[prefix_sum]
                start = P
                p_sum = prefix_sum
                
                # Remove all nodes between P and current
                while start != current:
                    start = start.next
                    p_sum += start.val
                    if start != current:
                        mp.pop(p_sum, None)
                
                P.next = start.next
            else:
                mp[prefix_sum] = current
            
            current = current.next
        
        return dummy.next
