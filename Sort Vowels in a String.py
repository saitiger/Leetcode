class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_set = set('aeiouAEIOU')
        vowels = [char for char in s if char in vowels_set]
        
        # Sort vowels by ASCII value
        vowels.sort()
        
        # Reconstruct string with sorted vowels
        result = []
        vowel_idx = 0
        
        for char in s:
            if char in vowels_set:
                result.append(vowels[vowel_idx])
                vowel_idx += 1
            else:
                result.append(char)
        
        return ''.join(result)
