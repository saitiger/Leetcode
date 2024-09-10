class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Solution 1 
        nums.sort()
        n = len(nums)-1
        return max(nums[0]*nums[1]*nums[n],nums[n-2]*nums[n-1]*nums[n])
        # Solution 2 
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])
