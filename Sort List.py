# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head
        while temp is not None:
            arr.append(temp.val)
            temp = temp.next
    
        arr.sort()
    
        temp = head
        for i in range(len(arr)):
            temp.val = arr[i]
            temp = temp.next
    
        return head

# Solution 2
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one node, return the head
        if head is None or head.next is None:
            return head

        def findMiddle(head: ListNode) -> ListNode:
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = ListNode()
            current = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            current.next = l1 if l1 else l2
            return dummy.next

        middle = findMiddle(head)
        right_head = middle.next
        middle.next = None

        left = self.sortList(head)
        right = self.sortList(right_head)

        return mergeTwoLists(left, right)
