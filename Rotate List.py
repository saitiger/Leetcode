# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return None
        
        lastElement = head
        length = 1

        while ( lastElement.next ):
            lastElement = lastElement.next
            length += 1

        k = k % length
            
        lastElement.next = head
        
        tempNode = head
        for _ in range( length - k - 1 ):
            tempNode = tempNode.next
        
        answer = tempNode.next
        tempNode.next = None
        
        return answer
