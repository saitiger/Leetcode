class Solution:
    def compressedString(self, word: str) -> str:
        i = 0
        res = []
    
        while i < len(word):
            current_char = word[i]
            count = 0
        
            while i < len(word) and word[i] == current_char and count < 9:
                count += 1
                i += 1
        
            res.append(str(count) + current_char)
    
        return ''.join(res)
