class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            cnt = 0
            arr = nums[:i]+nums[i+1:]
            for j in range(1,len(arr)):
                if(arr[j-1]<arr[j]):
                    cnt+=1
            if(cnt==len(arr)-1):
                return True
        return False
