class Solution:
    def isWinner(self, player1, player2):
        n = len(player1)
        p1Score = 0
        p2Score = 0
        
        for i in range(n):
            p1TurnScore = player1[i]
            p2TurnScore = player2[i]
            
            if (i == 1 and player1[0] == 10) or (i-2 >= 0 and (player1[i-1] == 10 or player1[i-2] == 10)):
                p1TurnScore *= 2
            if (i == 1 and player2[0] == 10) or (i-2 >= 0 and (player2[i-1] == 10 or player2[i-2] == 10)):
                p2TurnScore *= 2
                
            p1Score += p1TurnScore
            p2Score += p2TurnScore
            
        if p1Score > p2Score:
            return 1
        elif p2Score > p1Score:
            return 2
        else:
            return 0
