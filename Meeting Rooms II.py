"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        # The heap stores the end times of meetings
        heap = []
        
        # Add the first meeting. We need one room for the first meeting.
        heapq.heappush(heap, intervals[0].end)

        for i in intervals[1:]:
            # If the meeting starts after the earliest ending meeting
            # (i.e., there is no conflict, we can reuse the room)
            if heap[0] <= i.start:
                heapq.heappop(heap)  # Remove the room that is free

            heapq.heappush(heap, i.end)

        # The size of the heap is the minimum number of rooms required
        return len(heap)
