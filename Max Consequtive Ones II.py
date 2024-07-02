class Solution:
    def findMaxConsequtiveOnes(self, nums: List[int]) -> int:
        l = r = 0
        flip = 0
        max_len = 0
        while r<len(nums):
            if(nums[r]==0):
                flip+=1
            if(flip>1):
                while(nums[l]==0):
                    l+=1
                flip-=1
            max_len = max(max_len,(r-l+1))
            r+=1
            
        return max_len
