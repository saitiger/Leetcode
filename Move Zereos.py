# Solution 1 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0 
        for r in range(len(nums)):
            if(nums[r]!=0 and nums[l]==0):
                nums[l],nums[r] = nums[r],nums[l]
                l = l + 1
            if(nums[l]!=0):
                l = l + 1
                
# Solution 2 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        # while nums[l]!=0:
        #     l+=1
        #     break

        cnt = 0
        n = len(nums)
        l = 0
        for i in range(n):
            if nums[i]==0:
                cnt+=1
                l=i
                break 
        if cnt==0:
            return nums 
        else:
            r = l+1

            while r<n:
                if nums[r]!=0:
                    nums[l],nums[r] = nums[r],nums[l]
                    l+=1
                r+=1
            return nums
