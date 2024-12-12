# Solution 1 Sliding Window
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()  
        l,r = 0, 0
        max_len = 0
        
        # nums[l]+k>=nums[r]-k
        # nums[r]-nums[l]<=2*k
        
        while l< len(nums):
            while r < len(nums) and nums[r]-nums[l]<=2*k:
                r += 1
            max_len = max(max_len, r-l)
            l += 1
        return max_len

# Solution 2 : Using overlapping intervals
from collections import deque
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ranges = [(num - k, num + k) for num in nums]
        
        ranges.sort()
        
        max_beauty = 0
        deq = deque()
        
        for range_start, range_end in ranges:
            # Remove ranges that are no longer overlapping
            while deq and deq[0] < range_start:
                deq.popleft()            
            deq.append(range_end)
            max_beauty = max(max_beauty, len(deq))
        return max_beauty
