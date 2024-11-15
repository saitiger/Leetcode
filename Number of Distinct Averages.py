class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0,len(nums)-1
        avg_set = set()
        while i<len(nums) and j>0:   
            avg = (nums[i]+nums[j])/2
            avg_set.add(avg)
            i+=1
            j-=1
        return len(avg_set)
