class Solution:
    def thirdMax(self, nums):
        min_heap = []
        seen = set()

        for num in nums:
            if num not in seen:
                heapq.heappush(min_heap, num)
                seen.add(num)

                if len(min_heap) > 3:
                    smallest = heapq.heappop(min_heap)
                    seen.remove(smallest)

        # If we have 3 elements, the root is the third max
        if len(min_heap) == 3:
            return min_heap[0]
        else:
            # Otherwise return the max from what's left
            return max(min_heap)
