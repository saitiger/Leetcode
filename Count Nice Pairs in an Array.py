class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        temp = [n - int(str(n)[::-1]) for n in nums]
        cnt = {}
        ans = 0
        for t in temp:
            if t in cnt:
                ans+=cnt[t]
                cnt[t]+=1
            else:
                cnt[t]=1
        return ans%(10**9+7)
