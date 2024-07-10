class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            heappush(max_heap, diff)
            if len(max_heap) > ladders:
                bricks -= heappop(max_heap)
            if bricks < 0:
                return i
        return len(heights) - 1
