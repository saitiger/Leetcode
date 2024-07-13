class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x:x[1])
        cnt = 1
        end = pairs[0][1]
        for i in range(1,len(pairs)):
            if(pairs[i][0]>end):
                cnt+=1
                end = pairs[i][1]
        return cnt 
