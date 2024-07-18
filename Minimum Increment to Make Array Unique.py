class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0 
        for i in range(1,len(nums)):
            if(nums[i-1]>=nums[i]):
                cnt+=nums[i-1]-nums[i]+1
                nums[i] = nums[i-1]+1
        return cnt
# Count Sort 
        cnt = 0
        freq = [0] * (max(nums) + len(nums))
        for num in nums:
            freq[num]+= 1
        for i in range(len(freq)):
            if freq[i] > 1:
                freq[i + 1]+= freq[i] - 1
                cnt+= freq[i] - 1
        return cnt
