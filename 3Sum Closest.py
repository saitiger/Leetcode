class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                
                if current_sum > target:
                    r -= 1
                else:
                    l += 1
        
        return closest_sum
