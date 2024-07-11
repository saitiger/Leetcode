class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        cnt = {}
        res = []
        for n in nums:
            if n in cnt.keys():
                cnt[n]+=1
            else:
                cnt[n]=1
        for n in nums:
            if(cnt[n]==1):
                if(((n-1) not in cnt.keys()) and ((n+1) not in cnt.keys())):
                    res.append(n)
        return res

# One Liner 
        cnt = Counter(nums)
        return [n for n in nums if cnt[n] == 1 and cnt[n - 1] + cnt[n + 1] == 0]
      # Addition of both counts should be zero because none of the adjacent elements should exist in the array
