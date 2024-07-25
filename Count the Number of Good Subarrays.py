class Solution:
    def countGood(self, nums, k):
        head = 0
        tail = 0
        n = len(nums)
        mp = {}
        cnt = 0
        ans = 0
        while head < n:
            cnt += mp.get(nums[head], 0)
            mp[nums[head]] = mp.get(nums[head], 0) + 1
            while tail < head and cnt >= k:
                ans += n - head
                mp[nums[tail]] -= 1
                cnt -= mp.get(nums[tail], 0)
                tail += 1
            head += 1
        return ans
