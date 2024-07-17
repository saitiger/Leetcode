class Solution:
    def splitNum(self, num: int) -> int:
        digits = [n for n in str(num)]
        digits.sort()
        n = len(digits)
        num_1 = num_2 = ''
        for i in range(n):
            if(i%2==0):
                num_1 = num_1 + str(digits[i])
            else:
                num_2 = num_2 + str(digits[i])
        return int(num_1) + int(num_2)
