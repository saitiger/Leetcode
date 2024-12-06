# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1 : Brute Force 
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next 
        
        i,j = 0,len(arr)-1
        s = 0 
        while i<j:
            s = max(s,arr[i]+arr[j])
            i+=1
            j-=1
        return s

# Solution 2 
class Solution:
    # Helper functions 

    def reverse(self, head):
    # Reverse the Linked List
        prev = None
        curr = head
        while curr:
            nxt = curr.next  
            curr.next = prev  
            prev = curr       
            curr = nxt        
        return prev
    
    def middle(self,head):
    # Finding the middle using fast and slow pointer 
        if head is None:
            return None
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        return slow 
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        mid = self.middle(head) 
        second_part = self.reverse(mid) # Starting of the second half of the list after reversal
        res = 0 
        while second_part:
            res = max(res,head.val+second_part.val)
            head = head.next
            second_part = second_part.next
        return res
