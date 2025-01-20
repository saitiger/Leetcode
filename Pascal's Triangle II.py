# Solution 1 
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1] * (i + 1) for i in range(rowIndex+1)]
        for i in range(1, rowIndex+1):
            for j in range(1, i):
                result[i][j] = result[i - 1][j] + result[i - 1][j - 1]
        return result[rowIndex]

# Solution 2 
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        prev = []
        for i in range(rowIndex + 1):
            curr = [1] * (i + 1)
            for j in range(1, i):
                curr[j] = prev[j] + prev[j - 1]
            prev = curr
        return prev
