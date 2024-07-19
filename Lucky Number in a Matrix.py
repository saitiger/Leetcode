#BRUTE FORCE
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n_rows,n_cols = len(matrix),len(matrix[0])
        
        res = []
        row_min = set()

        for r in range(n_rows):
            row_min.add(min(matrix[r]))

        for c in range(n_cols):
            col_max = matrix[0][c]
            for r in range(n_rows):
                col_max = max(col_max,matrix[r][c])
            if col_max in row_min:
                res.append(col_max)

        return res

      #GREEDY
        n_rows,n_cols = len(matrix),len(matrix[0])

        max_row_min = float("-inf")
        
        for r in range(n_rows):
            row_min = min(matrix[r])
            max_row_min = max(row_min,max_row_min)

        for c in range(n_cols):
            col_max = matrix[0][c]
            for r in range(n_rows):
                col_max = max(col_max,matrix[r][c])
            if col_max ==max_row_min:
                return [col_max]
        
        return []
