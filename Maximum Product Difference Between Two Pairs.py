class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # Sorting 
        nums.sort()
        return nums[-1]*nums[-2] - nums[0]*nums[1]
        # Solution 2 - Without Sorting
        maxx = 0
        maxx_2 = 0
        minn = float('inf')
        minn_2 = float('inf')
        for num in nums:
            if num > maxx:
                maxx_2 = maxx
                maxx = num
            else:
                maxx_2 = max(maxx_2, num)
            if num < minn:
                minn_2 = minn
                minn = num
            else:
                minn_2 = min(minn_2, num)
        return maxx * maxx_2 - minn * minn_2
