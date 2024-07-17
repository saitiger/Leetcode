class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix), len(matrix[0])
        low,high = 0,r- 1
        while low <= high:
            row = (low + high) // 2
            if target > matrix[row][-1]:
                low = row + 1
            elif target < matrix[row][0]:
                high = row - 1
            else:
                break
        if not (low <= high):
            return False
        l, r = 0, c - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
