class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(-1,head)
        curr, prev = head, dummy
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if prev.next == curr:
                prev = prev.next
                curr = curr.next
            else:
                prev.next = curr.next
                curr = prev.next
        return dummy.next
