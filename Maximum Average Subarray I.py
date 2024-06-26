class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # currSum = maxSum = sum(nums[:k])
        # for i in range(k, len(nums)):
        # currSum += nums[i] - nums[i - k]
        # maxSum = max(maxSum, currSum)
        # return maxSum / k

        currSum = 0
        for n in nums[:k]:
            currSum += n
        maxSum = currSum 
        i = 0
        j = k
        while j < len(nums): 
            currSum -= nums[i] 
            i += 1 
            currSum += nums[j] 
            j += 1 
            maxSum = max(maxSum, currSum) 
        return maxSum / k 
