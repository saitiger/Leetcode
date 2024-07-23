class Solution:
    def isPathCrossing(self, path: str) -> bool:
        moves = {
            "N": (0, 1),
            "S": (0, -1),
            "W": (-1, 0),
            "E": (1, 0)
        }
        visited = set()
        x,y=0,0
        for c in path:
            visited.add((x, y))
            dx, dy = moves[c]
            x,y = x+dx,y+dy
            if (x, y) in visited:
                return True
        return False
