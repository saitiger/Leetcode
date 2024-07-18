class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rLen = len(matrix)
        cLen = len(matrix[0])
        rows = [False] * rLen
        cols = [False] * cLen
        for r in range(rLen):
            for c in range(cLen): 
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
        for i,v in enumerate(rows): 
            if r:
                for c in range(cLen):
                    matrix[i][c] = 0
        for j,v in enumerate(cols): 
            if v:
                for r in range(rLen):
                    matrix[r][j] = 0
# O(1) Solution 
        rLen, cLen = len(matrix), len(matrix[0])
        rowZero = False
        for r in range(rLen):
            for c in range(cLen):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        for r in range(1, rLen):
            for c in range(1, cLen):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(rLen):
                matrix[r][0] = 0
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
