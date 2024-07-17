class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen ={}
        ans = 0
        for n in nums:
            if n in seen:
                ans+=seen[n]
                seen[n]+=1
            else:
                seen[n]=1
        return ans
