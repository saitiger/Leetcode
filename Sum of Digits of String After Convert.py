class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ""
        for ch in s:
            char_int = ord(ch) - 96 # ASCII of 'a' is 97
            # char_int = ord(ch) - ord('a') + 1 
            num += str(char_int)
        
        while k>0:
            sum_digits = sum(int(ch) for ch in num)
            num = str(sum_digits)
            k-=1
        
        return int(num)
