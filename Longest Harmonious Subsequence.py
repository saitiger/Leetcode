class Solution:
    def findLHS(self, nums: List[int]) -> int:
       # Hashmap 
        mpp = defaultdict(int)
        ans = 0
        
        for n in nums:
            mpp[n]+=1

        for k in mpp:
            if k+1 in mpp:
                ans = max(ans, mpp[k] + mpp[k+1])
                
        return ans

  # Sorting and Sliding Window 
        nums.sort()
        res=l=0
        for r in range(len(nums)):
            while nums[r]-nums[l]>1:
                l+=1
            if nums[r]-nums[l]==1: res=max(res,r-l+1)
        return res
