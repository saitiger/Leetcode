class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        lsum = 0 
        cnt = 0

        for i in range(len(nums)-1):
            lsum+=nums[i]
            rsum = total - lsum
            if lsum>=rsum:
                cnt+=1
        return cnt
