class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minn = arrays[0][0]
        maxx = arrays[0][-1]

        res = 0

        for i in range(1, len(arrays)):
            currMin = arrays[i][0]
            currMax = arrays[i][-1]

            res = max(res, abs(currMin - maxx), abs(currMax - minn))

            maxx = max(maxx, currMax)
            minn = min(minn, currMin)
        
        return res
