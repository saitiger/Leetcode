class Solution:
    def firstCompleteIndex(self, arr, mat):
        m = len(mat)
        n = len(mat[0])

        index_map = {val: idx for idx, val in enumerate(arr)}

        min_index = float('inf')

        for row in mat:
            last_index = float('-inf') 
            for val in row:
                last_index = max(last_index, index_map[val])
            min_index = min(min_index, last_index)

        for col in range(n):
            last_index = float('-inf')  
            for row in range(m):
                val = mat[row][col]
                last_index = max(last_index, index_map[val])
            min_index = min(min_index, last_index)

        return min_index
