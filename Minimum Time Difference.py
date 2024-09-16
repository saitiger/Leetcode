class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_elapsed = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]

        time_elapsed.sort()

        ans = min(time_elapsed[i + 1] - time_elapsed[i] for i in range(len(time_elapsed) - 1))

        return min(ans, 24 * 60 - time_elapsed[-1] + time_elapsed[0])
