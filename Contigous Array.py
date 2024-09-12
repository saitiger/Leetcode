class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        mp = {}
        curr_sum = 0
        max_len = 0
        
        mp[0] = -1
        
        for i in range(n):
            curr_sum += 1 if nums[i] == 1 else -1
            if curr_sum in mp:
                max_len = max(max_len, i - mp[curr_sum])
            else:
                mp[curr_sum] = i
                
        return max_len
