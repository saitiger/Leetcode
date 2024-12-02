# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        temp = headA
        
        while temp:
            seen.add(temp)
            temp = temp.next
        
        temp = headB
        while temp:
            if temp in seen:
                return temp
            temp = temp.next

        return None        

# Solution 2 Credits : Striver 
        if not headA or not headB:
            return None
        
        d1 = headA
        d2 = headB
        
        while d1 != d2:
            # Move to the other list's head when reaching the end of a list
            d1 = headB if d1 is None else d1.next
            d2 = headA if d2 is None else d2.next
        
        # Either the intersection node or None (if no intersection exists)
        return d1
