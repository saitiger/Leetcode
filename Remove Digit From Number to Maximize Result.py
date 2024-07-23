class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        digits = []
        n = len(number)
        for i in range(n):
            if number[i] == digit:
                ans = number[0:i] + number[i+1:]
                digits.append(ans)
        maxi = digits[0]
        for digit in digits:
            if digit > maxi:
                maxi = digit
        return maxi
