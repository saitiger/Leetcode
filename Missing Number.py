class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      # Missing number using total sum   
      n = len(nums)
        total = (n*(n+1))/2
        s = sum(nums)
        return int(total - s)

      # XOR 
       # n = len(nums)
       # res = 0
        # for i in range(1,n+1):
            # res^ = i
        # for n in nums:
            # res^ = n
        # return res

    # Cyclic Sort 
        i = 0
        while i<len(nums):
            correct_idx = nums[i]
            if(correct_idx<len(nums) and nums[i]!=i):
                nums[i],nums[correct_idx] = nums[correct_idx],nums[i]
            else:
                i+=1
        
        for j in range(len(nums)):
            if(j!=nums[j]):
                return j
        return len(nums)
