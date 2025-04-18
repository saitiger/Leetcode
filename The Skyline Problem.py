from collections import defaultdict

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []

        for left, right, height in buildings:
            events.append((left, -height))   # Start of building
            events.append((right, height))   # End of building

        # Step 2: Sort events
        # If x is the same: (Solves edge cases when two same height occurs)
        #   - start events (-height) before end events (+height)
        #   - among starts: higher height first
        #   - among ends: lower height first

        events.sort()

        # Max heap and a height counter
        result = []
        heap = [0]  # Initial ground level
        height_count = defaultdict(int)
        height_count[0] = 1
        prev_max_height = 0

        for x, h in events:
            if h < 0:
                # Start of a building: push height to heap
                heapq.heappush(heap, h)
                height_count[-h] += 1
            else:
                # End of a building: reduce its count
                height_count[h] -= 1
                if height_count[h] == 0:
                    del height_count[h]

            # Clean up the heap: remove heights that are no longer active
            while -heap[0] not in height_count:
                heapq.heappop(heap)

            # Current max height
            current_max_height = -heap[0]

            # Add key point if height changed
            if current_max_height != prev_max_height:
                result.append([x, current_max_height])
                prev_max_height = current_max_height

        return result
