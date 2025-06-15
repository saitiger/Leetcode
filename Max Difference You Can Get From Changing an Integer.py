class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        
        # MAXIMIZE: replace the first digit that is not 9 with 9
        for digit in num_str:
            if digit != '9':
                max_str = num_str.replace(digit, '9')
                break
        else:
            max_str = num_str  # all digits are already 9

        max_num = int(max_str)

        # MINIMIZE
        # If first digit is not 1, replace it with 1 (safe for leading digit)
        if num_str[0] != '1':
            min_str = num_str.replace(num_str[0], '1')
        else:
            # Look for a later digit not 0 or 1 and replace it with 0
            for digit in num_str[1:]:
                if digit not in ['0', '1']:
                    min_str = num_str.replace(digit, '0')
                    break
            else:
                min_str = num_str  # nothing to minimize

        min_num = int(min_str)

        return max_num - min_num
