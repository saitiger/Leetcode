class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Create a min-heap with (value, index) pairs
        heap = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(heap)
        
        # Array used to mark the visited index
        marked = [False] * len(nums)
        score = 0

        while heap:
            value, index = heapq.heappop(heap)
            # If the index is already marked, skip it
            if marked[index]:
                continue
            score += value
            marked[index] = True
            if index > 0:
                marked[index - 1] = True
            if index < len(nums) - 1:
                marked[index + 1] = True
        
        return score
