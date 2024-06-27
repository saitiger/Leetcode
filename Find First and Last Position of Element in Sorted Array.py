class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums,target,True)
        right = self.binary_search(nums,target,False) 
        return [left,right]
    def binary_search(self,nums,target,left):
        l,r = 0,len(nums)-1
        idx = -1 # Initialized to -1 if we don't find instance of the element
        while l<=r:
            mid = l + (r-l)//2
            if(nums[mid]==target):
                idx = mid # Store the index if we don't find any more instance of the element
                if(left == True):
                    r = mid - 1  # Check the left hand side of the array to find the lowest index value for the occurence of the element
                else:
                    l = mid + 1
            elif(nums[mid]>target):
                r = mid - 1
            else:
                l = mid + 1
        return idx     
