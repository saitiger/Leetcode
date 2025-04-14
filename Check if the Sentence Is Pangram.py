class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        chk = [0]*26  

        for char in sentence:
            idx = ord(char) - ord('a') 
            chk[idx] = 1  # Mark as seen

        return sum(chk) == 26
