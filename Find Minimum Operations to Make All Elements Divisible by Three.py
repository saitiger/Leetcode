class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # ops = 0
        # for n in nums:
        #     if n%3!=0:
        #         ops+=1
        # return ops

        ops = 0 
        for n in nums:
            ops+= min(n % 3, 3 - (n % 3))
        return ops
