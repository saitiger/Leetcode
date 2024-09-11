class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        cur = 0
        n = len(nums)
        temp = [0] * (n + 1)
        
        for i in range(n):
            cur += temp[i]
            nums[i] -= cur
            if nums[i] < 0:
                return False
            cur += nums[i]
            
            if (i + k) <= n:
                temp[i + k] -= nums[i]
                nums[i] = 0
        
        for i in range(n):
            if nums[i] != 0:
                return False
        
        return True
