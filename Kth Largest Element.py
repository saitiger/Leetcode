class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       # Solution 1
        
        nums.sort()
        return nums[len(nums) - k]

        # Solution 2 
        heapq._heapify_max(nums)
        while k>1:
            heapq._heappop_max(nums)
            k-=1
        return nums[0]
