class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        lsum = 0
        total = sum(nums)

        for i in range(n):
            rsum = total - lsum - nums[i]
            if(rsum==lsum):
                return i 
            lsum+=nums[i]

        return -1
