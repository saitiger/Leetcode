class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.m = 0
        self.n = 0

    def DFS(self, grid, i, j, visited):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or visited[i][j] or grid[i][j] == 0:
            return
        
        visited[i][j] = True  # mark as visited

        for dir in self.directions:
            new_i = i + dir[0]
            new_j = j + dir[1]
            self.DFS(grid, new_i, new_j, visited)

    def numberOfIslandsDFS(self, grid):
        visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        islands = 0

        for i in range(self.m):
            for j in range(self.n):
                if not visited[i][j] and grid[i][j] == 1:
                    self.DFS(grid, i, j, visited)
                    islands += 1

        return islands

    def minDays(self, grid):
        self.m = len(grid)
        self.n = len(grid[0])
        islands = self.numberOfIslandsDFS(grid)

        # Grid already disconnected
        if islands > 1 or islands == 0:
            return 0
        else:
            # Check if it can be disconnected with 1 move
            for i in range(self.m):
                for j in range(self.n):
                    if grid[i][j] == 1:
                        grid[i][j] = 0  # set as water
                        islands = self.numberOfIslandsDFS(grid)
                        grid[i][j] = 1  # revert to land
                        if islands > 1 or islands == 0:
                            return 1

        return 2  # It's always possible to break an island with 2 moves
