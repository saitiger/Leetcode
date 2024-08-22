class Solution:
    def getLeftMax(self, height, n):
        leftMax = [0] * n
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        return leftMax

    def getRightMax(self, height, n):
        rightMax = [0] * n
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        return rightMax

    def trap(self, height):
        n = len(height)
        if n == 0 or n == 1:
            return 0
        
        leftMax = self.getLeftMax(height, n)
        rightMax = self.getRightMax(height, n)

        total_water = 0
        for i in range(n):
            total_water += min(leftMax[i], rightMax[i]) - height[i]
        
        return total_water
