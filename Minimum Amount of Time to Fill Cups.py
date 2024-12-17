class Solution:
    def fillCups(self, amount):
        max_heap = [-a for a in amount if a > 0]
        heapq.heapify(max_heap)
        seconds = 0
        while max_heap:
        # Case 1: More than one cup type left
            if len(max_heap) >= 2:
                first = -heapq.heappop(max_heap)
                second = -heapq.heappop(max_heap)
                first -= 1
                second -= 1
                if first > 0: heapq.heappush(max_heap, -first)
                if second > 0: heapq.heappush(max_heap, -second)
            else:
        # Case 2: Only one cup type left
                seconds += -heapq.heappop(max_heap)
                break
            seconds += 1
        return seconds
