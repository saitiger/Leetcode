class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import defaultdict

        n = len(grid)
        count = 0
        mp = defaultdict(int)
        
        for row in grid:
            mp[tuple(row)] += 1
        
        for c in range(n):
            temp = []
            for r in range(n):
                temp.append(grid[r][c])
            
            count += mp[tuple(temp)]
        
        return count
