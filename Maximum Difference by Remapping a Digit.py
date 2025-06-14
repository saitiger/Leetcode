class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_num = [n for n in str(num)]
        min_num = [n for n in str(num)]

        # Replace the most significant digit that is not '9' with '9'
        # Replace all occurrences of first non-'9' digit with '9'
        changed_digit = None
        for i in range(len(max_num)):
            if changed_digit is None and max_num[i] != '9':
                changed_digit = max_num[i]
            if changed_digit is not None and max_num[i] == changed_digit:
                max_num[i] = '9'

        # Replace the most significant digit that is not '0' with '0' 
        # Replace all occurrences of first non-'0' digit with '0'
        changed_digit_min = None
        for j in range(len(min_num)):
            if changed_digit_min is None and min_num[j] != '0':
                changed_digit_min = min_num[j]
            if changed_digit_min is not None and min_num[j] == changed_digit_min:
                min_num[j] = '0'

        max_val = int("".join(max_num))
        min_val = int("".join(min_num))
        return max_val - min_val
