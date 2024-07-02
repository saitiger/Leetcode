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
