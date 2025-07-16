class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Case 1: all even
        even_only = [num for num in nums if num % 2 == 0]
        # Case 2: all odd
        odd_only = [num for num in nums if num % 2 == 1]

        max_len = max(len(even_only), len(odd_only))

        # Case 3: longest alternating parity subsequence        
        alt_len = 1
        curr_parity = nums[0] % 2
        
        for i in range(1, len(nums)):
            next_parity = nums[i] % 2
            if next_parity != curr_parity:
                alt_len += 1
                curr_parity = next_parity

        return max(max_len, alt_len)
