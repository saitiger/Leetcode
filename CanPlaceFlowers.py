class Solution:
    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:
        for i in range(len(nums)):
            if nums[i]==0:
                if(i==0 or nums[i-1]==0) and (i==len(nums)-1 or nums[i+1]==0):
                    n-=1
                    nums[i]=1
            if n<=0:
                return True
        return False
