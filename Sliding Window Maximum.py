class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
# Solution 1 
        max_heap = []
        result = []
        
        for i in range(len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))
            
            if i >= k - 1:
                while max_heap[0][1] <= i - k:
                    heapq.heappop(max_heap)
                
                result.append(-max_heap[0][0])

        return result
# Solution 2 
from collections import deque
        n = len(nums)
        if n == 0:
            return []
        
        deq = deque()  
        result = []
        
        for i in range(n):
            while deq and deq[0] <= i - k:
                deq.popleft()
            
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            
            deq.append(i)
            
            if i >= k - 1:
                result.append(nums[deq[0]])
        
        return result
