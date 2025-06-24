class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = [0] * 26
        
        for ch in word:
            freq[ord(ch) - ord('a')] += 1
        
        result = len(word)
        
        for i in range(26):
            del_count = 0
            
            for j in range(26):
                if i == j:
                    continue
                
                if freq[j] < freq[i]:
                    del_count += freq[j]
                elif abs(freq[j] - freq[i]) > k:
                    del_count += abs(freq[j] - freq[i] - k)
            
            result = min(result, del_count)
        
        return result
