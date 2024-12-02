# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(head):
            temp = head
            prev = None
            while temp is not None:
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front
            return prev

        def getKthNode(temp, k):
            k -= 1
            while temp is not None and k > 0:
                k -= 1
                temp = temp.next
            return temp

        temp = head
        prevLast = None

        while temp is not None:
            kThNode = getKthNode(temp, k)

            # If there are fewer than k nodes left, link the remainder and exit
            if kThNode is None:
                if prevLast:
                    prevLast.next = temp
                break

            # Store the node after the k-th node
            nextNode = kThNode.next

            # Disconnect the k-th node to prepare for reversal
            kThNode.next = None
            reverseLinkedList(temp)

            # Update the head if the reversal includes the initial head
            if temp == head:
                head = kThNode
            else:
                prevLast.next = kThNode

            # Update the pointer to the last node of the reversed group
            prevLast = temp
            temp = nextNode

        return head        
