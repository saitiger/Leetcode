class Solution:
    def minTimeToVisitAllPoints(self, points):
        n = len(points)
        steps = 0
        
        for i in range(n - 1): 
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            
            diagonal = min(dx, dy)
            remain = abs(dx - dy)
            
            steps += diagonal + remain
        
        return steps
