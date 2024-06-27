class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0 
        mx_cnt = 0 

        for i in range(len(nums)):
            if(nums[i]==1):
                cnt = cnt + 1
                mx_cnt = max(cnt,mx_cnt)
            else : 
                cnt = 0 
        return mx_cnt 
