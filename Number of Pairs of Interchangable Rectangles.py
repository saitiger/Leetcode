class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        seen ={}
        ans = 0
        for r in rectangles:
            if r[0]/r[1] in seen:
                ans+=seen[r[0]/r[1]]
                seen[r[0]/r[1]]+=1
            else:
                seen[r[0]/r[1]]=1
        return ans
