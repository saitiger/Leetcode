class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr_sum,max_sum = nums[0],nums[0]
        max_num = max(nums) 
        # In the case when none of the elements are in increasing order
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                curr_sum+=nums[i]
                max_sum = max(max_sum,curr_sum)
            else:
                curr_sum = nums[i]
        return max_sum if max_sum>max_num else max_num

        # Solution 2 
        curr_sum,max_sum = nums[0],0
        for i in range(1,len(nums)):
            if nums[i-1]>=nums[i]:
                max_sum = max(max_sum,curr_sum)
                curr_sum = 0
            curr_sum+=nums[i]
        return max(max_sum,curr_sum)
