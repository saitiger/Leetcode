class Solution:
    def countDigits(self, num: int) -> int:
        num1 = num 
        digits = []

        while num1:
            digit = num1%10
            num1 = num1//10
            digits.append(digit)

        digits = digits[::-1]    

        cnt = 0
        for d in digits:
            if num%d==0:
                cnt+=1
        return cnt 
