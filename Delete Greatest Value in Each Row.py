class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        # Sort each row
        for i in range(row):
            grid[i].sort()
        ans = 0
        # Iterate each column from the back since we are extracting the maximum of each row 
        for j in range(col):
            maxi = float('-inf') # Initialize 
            for i in range(row):
                maxi = max(maxi, grid[i][j]) # Find the column maximum 
            ans += maxi
        return ans
