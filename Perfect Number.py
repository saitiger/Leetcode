class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False  
        s = 1  
        max_check = int(num**(1/2))
        
        for i in range(2, max_check + 1):
            if num % i == 0:  
                s += i
                if i != num // i:  # Avoid adding the square root twice for perfect squares
                    s += num // i
        return s == num
