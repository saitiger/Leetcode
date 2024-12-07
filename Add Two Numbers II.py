# Solution 1 
class Solution:
    def reverseLL(self, head):
        if not head or not head.next:
            return head
        
        last = self.reverseLL(head.next)
        head.next.next = head
        head.next = None
        return last
    
    def addTwoNumbers(self, l1, l2):
        l1 = self.reverseLL(l1)
        l2 = self.reverseLL(l2)
        
        sum = 0
        carry = 0
        ans = ListNode()
        
        while l1 or l2:
            if l1:
                sum += l1.val
                l1 = l1.next
            
            if l2:
                sum += l2.val
                l2 = l2.next
            
            ans.val = sum % 10
            carry = sum // 10
            
            new_node = ListNode(carry)
            new_node.next = ans
            ans = new_node
            sum = carry
        
        return ans.next if carry == 0 else ans

# Solution 2 : Using Stack 
class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1, stack2 = [], []
        
        # Push all values of l1 into stack1
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        # Push all values of l2 into stack2
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        sum = 0
        carry = 0
        ans = ListNode()
        
        # Process stacks until both are empty
        while stack1 or stack2:
            if stack1:
                sum += stack1.pop()
            if stack2:
                sum += stack2.pop()
            
            ans.val = sum % 10
            carry = sum // 10
            
            new_node = ListNode(carry)
            new_node.next = ans
            ans = new_node
            sum = carry
        
        return ans.next if carry == 0 else ans
