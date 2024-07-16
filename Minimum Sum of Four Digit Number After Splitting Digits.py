class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []

        for n in str(num):
            digits.append(n)

        digits.sort()

        new_1 = digits[0]+digits[2]
        new_2 = digits[1]+digits[3]
        return int(new_1)+int(new_2)
