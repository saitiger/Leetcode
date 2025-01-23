class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
      """
      
      Count the number of servers in each row and column.
      In the next iteration for each cell that has a server if the row or column of that corresponding server has another server then increment the count
      
      """
      
        rows = len(grid)
        cols = len(grid[0])
        row_cnt = [0] * rows  # Number of servers in each row 
        col_cnt = [0] * cols  # Number of servers in each column 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    row_cnt[r] += 1
                    col_cnt[c] += 1

        cnt = 0 
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:  # If server exists 
                    if row_cnt[r] > 1 or col_cnt[c] > 1:  # Increment count if there is another server in the same row or column
                        cnt += 1
        return cnt
