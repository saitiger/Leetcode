class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        result = []
        
        top, down = 0, m - 1
        left, right = 0, n - 1
        
        while top <= down and left <= right:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            for i in range(top, down + 1):
                result.append(matrix[i][right])
            right -= 1
            
            if top <= down:
                for i in range(right, left - 1, -1):
                    result.append(matrix[down][i])
                down -= 1
            
            if left <= right:
                for i in range(down, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result


# Cleaner Code (NeetCode)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
