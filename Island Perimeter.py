class Solution:
    def islandPerimeter(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                
                if i - 1 < 0 or grid[i - 1][j] == 0:  # up
                    perimeter += 1
                
                if i + 1 >= m or grid[i + 1][j] == 0:  # down
                    perimeter += 1
                
                if j - 1 < 0 or grid[i][j - 1] == 0:  # left
                    perimeter += 1
                
                if j + 1 >= n or grid[i][j + 1] == 0:  # right
                    perimeter += 1
        
        return perimeter
