class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        current_sum = 0
        num_set = set()
        start = 0  
        for end in range(len(nums)):
            current_num = nums[end]
            
            while current_num in num_set:
                left_num = nums[start]
                current_sum -= left_num
                num_set.remove(left_num)
                start += 1

            num_set.add(current_num)
            current_sum += current_num

            if end - start + 1 == k:
                max_sum = max(max_sum, current_sum)
                
                left_num = nums[start]
                current_sum -= left_num
                num_set.remove(left_num)
                start += 1

        return max_sum
