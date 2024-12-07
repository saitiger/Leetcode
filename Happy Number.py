class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()  
        while n != 1:  
            sum_of_squares = 0
            while n > 0:
                digit = n % 10
                sum_of_squares += digit ** 2
                n //= 10
            if sum_of_squares in visited:
                return False
            visited.add(sum_of_squares)            
            n = sum_of_squares
        return True
        
# Solution 2 : Using Linked List Cycle Detection
class Solution:
    def isHappy(self, n: int) -> bool:
        def squared(n):
            result = 0
            while n>0:
                last = n%10
                result += last * last
                n = n//10
            return result
        
        slow = squared(n)
        fast = squared(squared(n))

        while slow!=fast and fast!=1:
            slow = squared(slow)
            fast = squared(squared(fast))

        return fast==1
