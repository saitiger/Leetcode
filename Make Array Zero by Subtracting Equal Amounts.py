class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if all(n == 0 for n in nums):
            return 0       
        steps = 0
        while any(n > 0 for n in nums):
            curr_min = min(n for n in nums if n > 0)
            nums = [n - curr_min if n > 0 else 0 for n in nums]
            steps += 1
        return steps

      # Solution 2 Using Set
        unique_positive_values = set(n for n in nums if n > 0)
        return len(unique_positive_values)
