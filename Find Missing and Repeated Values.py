from collections import defaultdict
class Solution:
    def findMissingAndRepeatedValues(self, v):
        n = len(v)
        m = defaultdict(int)
        for i in range(n):
            for j in range(n):
                m[v[i][j]] += 1
        a, b = -1, -1
        for i in range(1, n * n + 1):
            if m[i] == 2:
                a = i
            elif m[i] == 0:
                b = i
        return [a, b]

# Solution 2 : Math 
        n = len(grid)
        total = n * n

        sum_val = sum(num for row in grid for num in row)
        sqr_sum = sum(num * num for row in grid for num in row)

        sum_diff = sum_val - total * (total + 1) // 2
        sqr_diff = sqr_sum - total * (total + 1) * (2 * total + 1) // 6

        repeat = (sqr_diff // sum_diff + sum_diff) // 2
        missing = (sqr_diff // sum_diff - sum_diff) // 2

        return [repeat, missing]
