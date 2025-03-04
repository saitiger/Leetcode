class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
"""
Base 10 to Base n : Keep dividing by n. Remainders in the reverse order is the Base n representation
Check if the Base 3 representation only contains 0s and 1s. If there is a 2, it means we need two of some power of 3, which breaks the rule of using distinct powers.
"""
        # Convert to Base 3 
        while n>0:
            if n%3==2: # Should  contain only 0s or 1s 
                return False
            n//=3
        return True
