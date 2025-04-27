"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort by start time
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            # If the end of the previous interval is greater than the current interval's start time, it's a conflict
            if intervals[i-1].end > intervals[i].start:
                return False
        return True
