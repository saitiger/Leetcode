class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)  
        first_idx, last_idx = 0, len(s) - 1

        while first_idx < last_idx:
            while first_idx < last_idx and s[first_idx] not in vowels:
                first_idx += 1
            while first_idx < last_idx and s[last_idx] not in vowels:
                last_idx -= 1

            s[first_idx], s[last_idx] = s[last_idx], s[first_idx]
            first_idx += 1
            last_idx -= 1

        return ''.join(s)
