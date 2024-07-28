from collections import deque

class Solution:
    def findEquationValue(self, P1, P2, P3):
        x1, y1 = P1
        x2, y2 = P2
        x3, y3 = P3
        
        return (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)
    
    def outerTrees(self, trees):
        trees.sort()
        
        upper = deque()
        lower = deque()
        
        for point in trees:
            while len(lower) >= 2 and self.findEquationValue(lower[-2], lower[-1], point) < 0:
                lower.pop()
            while len(upper) >= 2 and self.findEquationValue(upper[-2], upper[-1], point) > 0:
                upper.pop()
            lower.append(point)
            upper.append(point)
        
        result_set = set(tuple(p) for p in upper) | set(tuple(p) for p in lower)
        result = [list(p) for p in result_set]
        
        return result
