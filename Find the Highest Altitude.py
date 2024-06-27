class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curSum = 0 
        max_gain = 0 
        for n in gain:
            curSum+=n
            max_gain = max(max_gain,curSum)
        return max_gain
