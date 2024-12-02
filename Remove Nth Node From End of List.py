# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1 
def DeleteNthNodefromEnd(head, N):
    if head is None:
        return None

    # Count the number of nodes in the linked list
    cnt = 0
    temp = head
    while temp:
        cnt += 1
        temp = temp.next

    # If N equals the total number of nodes, delete the head
    if cnt == N:
        newhead = head.next
        return newhead

    # Calculate the position of the node just before the one to delete
    res = cnt - N
    temp = head

    # Traverse to the node just before the one to delete
    for _ in range(res - 1):
        temp = temp.next

    # Delete the Nth node from the end
    temp.next = temp.next.next
    return head

# Solution 2 Using Fast and Slow Pointer (Credits : Striver) : Learnt the concept of Fast and Slow Pointer for One Pass algorithm
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fastp = head
        slowp = head

        # Move the fastp pointer n nodes ahead
        for i in range(n):
            if fastp is None:  # Handle edge case if n is larger than the length of the list
                return head
            fastp = fastp.next

        # If fastp becomes None, the Nth node from the end is the head
        if fastp is None:
            return head.next

        # Move both pointers until fastp reaches the end
        while fastp.next is not None:
            fastp = fastp.next
            slowp = slowp.next

        # Delete the Nth node from the end
        slowp.next = slowp.next.next
        return head
