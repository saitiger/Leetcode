class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if(nums[mid]==target):
                return mid 
            elif(nums[mid]<target):
                l = mid + 1
            else:
                r = mid - 1
        return l # Return left pointer because when right crosses left that is 
                #  when we know that we have either crossed the length of the array or we have found the insert position
