class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(number):
            temp = number
            while temp > 0:
                digit = temp % 10
                if digit == 0 or number % digit != 0:
                    return False
                temp //= 10
            return True

        result = []
        for num in range(left, right + 1):
            if is_self_dividing(num):
                result.append(num)
        return result
