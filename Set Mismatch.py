class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing, repeat = 0, 0
        s = 0
        n = len(nums)
        actual_sum = n * (n + 1) // 2
        seen = set()

        for i in nums:
            if i in seen:
                repeat = i # The number that is already in set seen is the value that is repeated.
            else:
                seen.add(i)
                s+=i

        missing = actual_sum - s # Missing number is sum on natural numbers - sum we have (after removing the duplicate i.e using set)
        return [repeat, missing]
      
      # Cyclic Sort 
        i = 0
        while i<len(nums):
            correct_idx = nums[i] - 1 
            if(correct_idx<len(nums) and nums[i]!=nums[correct_idx]):
                nums[i],nums[correct_idx] = nums[correct_idx],nums[i]
            else:
                i+=1
        for j in range(len(nums)):
            if(nums[j]!=j+1):
                return [nums[j],j+1]
