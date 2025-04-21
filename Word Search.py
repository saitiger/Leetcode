class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, l = len(board), len(board[0]), len(word)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def find(i, j, idx):
            if idx == l:
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[idx]:
                return False

            temp = board[i][j]
            board[i][j] = '#'  # mark as visited

            for dx, dy in directions:
                if find(i + dx, j + dy, idx + 1):
                    return True

            board[i][j] = temp  # backtrack
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and find(i, j, 0):
                    return True

        return False
