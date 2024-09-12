class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        rem = total - x
        
        if rem == 0:
            return n

        length = self.maxSubArrayLen(rem, nums)

        if length == 0:
            return -1
        
        return n - length

    def maxSubArrayLen(self, k: int, A: List[int]) -> int:
        sum_ = 0
        res = 0
        mp = defaultdict(int)
        mp[0] = -1

        for i in range(len(A)):
            sum_ += A[i]
            if (sum_ - k) in mp:
                res = max(res, i - mp[sum_ - k])
            
            if sum_ not in mp:
                mp[sum_] = i
        
        return res
