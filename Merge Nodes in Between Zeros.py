class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        start = head.next
        end = start

        while end:
            s = 0 # Accumulate the sum until a 0 is encountered
            while end and end.val != 0:
                s += end.val
                end = end.next

            start.val = s
            # Skip the zero node
            end = end.next
            # Update the start's next pointer
            start.next = end
            start = start.next
        return head.next
