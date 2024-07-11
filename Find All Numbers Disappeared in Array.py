class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
      # Brute Force 
        d = {}
        for i in range(1, len(nums)+1):  
            d[i] = 0
        for i in nums:
            d[i] += 1
        result = []
        for key, val in d.items():
            if val == 0:
                result.append(key)
        return result
      
      # Negative Marking 
      n = len(nums)
        nums.sort()
        res = [0]*n
        final = []
        for v in nums:
            res[v-1] = 1

        for i in range(n):
            if(res[i]==0):
                final.append(i+1)
        return final

  # Cyclic Sort 
        i = 0
        res = []
        while i<len(nums):
            correct_idx = nums[i] - 1 
            if(correct_idx<len(nums) and nums[i]!=nums[correct_idx]):
                nums[i],nums[correct_idx] = nums[correct_idx],nums[i]
            else:
                i+=1
        for j in range(len(nums)):
            if(j+1!=nums[j]):
                res.append(j+1)
        return res
