class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        cnt = sum(nums)
        if cnt == 0:  # If there are no 1s in the array
            return 0

        m = len(nums)
        i, j, res, cnt_zero = 0, 0, float('inf'), 0

        while j < 2 * m:
            if nums[j % m] == 0:
                cnt_zero += 1
            if j - i + 1 == cnt:
                res = min(res, cnt_zero)
                if nums[i % m] == 0:
                    cnt_zero -= 1
                i += 1
            j += 1
        return res

class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        
        countOnes = sum(nums)
        
        i = 0
        j = 0
        currCount = 0
        maxCount = 0
        
        while j < 2 * n:
            if nums[j % n] == 1:
                currCount += 1
            
            if j - i + 1 == countOnes:
                maxCount = max(maxCount, currCount)
                currCount -= nums[i % n]
                i += 1
            j += 1
        
        return countOnes - maxCount
