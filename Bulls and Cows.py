class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        lookup = Counter(secret)
        
        bulls, cows = 0, 0
        
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bulls+=1
                lookup[secret[i]]-=1
        
        for i in range(len(guess)):
            if guess[i] in lookup and secret[i] != guess[i] and lookup[guess[i]]>0:
                cows+=1
                lookup[guess[i]]-=1
    		
        return "{}A{}B".format(bulls, cows)
