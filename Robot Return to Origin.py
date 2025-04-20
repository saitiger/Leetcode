class Solution:
    def judgeCircle(self, moves: str) -> bool:
      # Solution 1 : Keeping track of number of moves 
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
      # Solution 2 : Simulation 
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1
        return x == y == 0
