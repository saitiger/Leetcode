class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        mpp = defaultdict(int)
        zero_loss,one_loss = [],[]

        for i in range(len(matches)):
            mpp[matches[i][1]]+=1

        for i in range(len(matches)):
            winner = matches[i][0]
            loser = matches[i][1]
            if winner not in mpp.keys():
                zero_loss.append(winner)
                mpp[winner] = 2
            if mpp[loser]==1:
                one_loss.append(loser)

        zero_loss.sort()   
        one_loss.sort()
          
        return [zero_loss,one_loss] 
