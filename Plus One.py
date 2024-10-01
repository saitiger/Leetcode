# Brute Force 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        num = 0
        
        for i in range(n):
            num+= digits[i]*(10**(n-i-1))

        res = num+1

        ans = []
        while res:
            d = res%10
            res = res//10
            ans.append(d)
        return ans[::-1]

# Solution 2 
        for i in range(len(digits) - 1, -1, -1):

            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            
            digits[i] = 0

            if i == 0:
                return [1] + digits
