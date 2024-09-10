class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        columns = len(matrix[0])
        ans =[[0]*rows for _ in range(columns)] # Initialing an array 
        for r in range(rows):
            for c in range(columns):
                # Swap [r][c] with [c][r]. This keeps the diagonals at the same place
                ans[c][r] = matrix[r][c]
        return ans
