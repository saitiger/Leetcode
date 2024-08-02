class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        cnt = 0
        m = len(nums)
        for n in nums:
            if n==1:
                cnt+=1

        if cnt==0:
            return 0
        
        i,j,res,cnt_zero = 0,0,float(inf),0

        while j<m:
            if nums[j]==0:
                cnt_zero+=1
            if(j-i+1==cnt):
                res = min(res,cnt_zero)
                if (nums[i]==0):
                    cnt_zero-=1
                i+=1
            j+=1
        return res
