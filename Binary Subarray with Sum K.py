class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
# Solution 1 
        prefix_zeros = 0
        window_sum = 0
        count = 0

        i = 0
        j = 0
        
        while j < len(nums):
            window_sum += nums[j]
            
            while i < j and (nums[i] == 0 or window_sum > goal):
                if nums[i] == 1:
                    prefix_zeros = 0
                else:
                    prefix_zeros += 1
                
                window_sum -= nums[i]
                i += 1
            
            if window_sum == goal:
                count += 1 + prefix_zeros
            
            j += 1
        
        return count
# Solution 2 
    def helper_func(self, nums: List[int], goal: int) -> int:

        start, current_sum, total_count = 0, 0, 0

        for end in range(len(nums)):
            current_sum += nums[end]

            while start <= end and current_sum > goal:
                current_sum -= nums[start]
                start += 1

            total_count += end - start + 1

        return total_count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.helper_func(nums, goal) - self.helper_func(nums, goal - 1)
