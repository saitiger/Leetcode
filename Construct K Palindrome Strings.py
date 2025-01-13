class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        
        if n < k:
            return False
        
        if n == k:
            return True
        
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        odd_freq_char_count = sum(1 for count in freq if count % 2 != 0)
        
        return odd_freq_char_count <= k
