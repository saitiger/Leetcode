class Solution:
    def minimumSteps(self, s: str) -> int:
        cnt,swaps = 0,0
        for ball in s:
            if ball=="1":
                cnt+=1
            else:
                swaps+=cnt
        return swaps
