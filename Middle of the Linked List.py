class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        len_ll = 0
        if head is None or head.next is None:
            return head
        while temp is not None:
            len_ll += 1
            temp = temp.next
        target = len_ll // 2 + 1
        temp = head
        while target:
            target -= 1
            if target ==0:
                break
            temp = temp.next
        return temp

  # Solution 2 
        if head is None or head.next is None:
            return head
        fast,slow = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
