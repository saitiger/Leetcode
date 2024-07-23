class Solution:
    def heightChecker(self, heights):
        min_height = min(heights)
        max_height = max(heights)
        count = [0] * (max_height + 1)
        for height in heights:
            count[height] += 1
        expected = heights[:]
        i = 0
        for val in range(min_height, max_height + 1):
            while count[val] > 0:
                expected[i] = val
                count[val] -= 1
                i += 1
        ans = 0
        for x in range(len(heights)):
            if expected[x] != heights[x]:
                ans += 1
        return ans
