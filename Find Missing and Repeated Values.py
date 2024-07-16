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
