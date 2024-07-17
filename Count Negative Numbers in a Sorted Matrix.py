class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Solution 1 : Binary Search 
        count  = 0
        cols = len(grid[0])
        for row in grid:
            left, right = 0 , cols - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] < 0: 
                    count += right - mid + 1
                    right = mid - 1
                else: left = mid + 1
        return count  
      
        # Solution 2 
        n = len(grid)
        r,c = 0,len(grid[0])-1
        cnt = 0
        while c>= 0 and r<n:
            if grid[r][c] < 0:
                cnt+= n - r
                c-= 1
            else:
                r+= 1
        return cnt
