class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        mp = defaultdict(int)
        sum_ = 0
        result = 0
        
        mp[0] = 1
        
        for num in nums:
            sum_ += num
            rem = sum_ % k
            
            if rem < 0:
                rem += k
            
            if rem in mp:
                result += mp[rem]
            
            mp[rem] += 1
        
        return result
