class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        current = head
        while current:
            copy = Node(current.val)
            copy.next = current.next
            current.next = copy
            current = copy.next

        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        current = head
        dummy = Node(0)
        copy_tail = dummy

        while current:
            copy = current.next
            current.next = copy.next  
            copy_tail.next = copy  
            copy_tail = copy
            current = current.next

        return dummy.next
