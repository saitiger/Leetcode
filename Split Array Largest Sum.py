# The intuition is that the minimum possible value for our answer is the largest individual greatest value since that is our bottleneck or controlling factor i.e. search range
# starts from max(nums) and extends till sum(nums) as the whole array is also a valid subarray.
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def canSplit(largest): # Validating if number of subarrays is lesser than the problem constraint
            subarray = 1 # Initiliaze with 1 as empty subarray is also a valid answer
            curSum = 0
            for n in nums:
                curSum += n # Prefix Sum to check if the the subarray is still valid 
                if curSum > largest:
                    subarray += 1
                    curSum = n
            return subarray<= m

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + ((r - l) // 2)
            if canSplit(mid): # If split is valid store as answer and look for smaller values 
                res = mid
                r = mid - 1
            else:
                l = mid + 1 # If split is not valid look for smaller values 
        return res
