"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        current = head
        
        while current is not None:
            if current.child is not None:
                self.merge(current)
            current = current.next
        
        return head
            
    
    def merge(self, current):
        child = current.child
        
        while child.next is not None:
            child = child.next
        
        if current.next is not None:
            child.next = current.next
            current.next.prev = child
        
        current.next = current.child
        current.child.prev = current
        
        current.child = None        
