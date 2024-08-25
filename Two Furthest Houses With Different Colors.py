class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        i, j = 0, n - 1
        
        while i < n:
            if colors[n - 1] == colors[i]:
                i += 1
            else:
                return n - 1 - i
            
            if colors[j] == colors[0]:
                j -= 1
            else:
                return j
        
        return -1
