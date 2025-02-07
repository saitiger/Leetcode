class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Create max heap with (value, index) pairs
        max_heap = [(-val, i) for i, val in enumerate(nums)]
        heapq.heapify(max_heap)
    
        # Get indices of k largest elements
        indices = []
        while k:
            val, idx = heapq.heappop(max_heap)
            indices.append(idx)
            k -= 1
    
        # Sort indices to maintain original order
        indices.sort()
    
        # Return values at those indices
        return [nums[i] for i in indices]
