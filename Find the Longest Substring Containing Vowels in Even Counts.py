class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Dictionary to map the state (parity of vowels) to the first occurrence index
        state_map = {}
        
        # Initialize a list to track the count of each vowel ('a', 'e', 'i', 'o', 'u')
        vowel_count = [0] * 5  # Parity of 'a', 'e', 'i', 'o', 'u'
        
        current_state = "00000"  # Initial state where all vowels have even counts
        state_map[current_state] = -1  # Initial state maps to index -1
        
        max_length = 0
        
        for i, char in enumerate(s):
            # Update the parity of the vowel encountered
            if char == 'a':
                vowel_count[0] = (vowel_count[0] + 1) % 2
            elif char == 'e':
                vowel_count[1] = (vowel_count[1] + 1) % 2
            elif char == 'i':
                vowel_count[2] = (vowel_count[2] + 1) % 2
            elif char == 'o':
                vowel_count[3] = (vowel_count[3] + 1) % 2
            elif char == 'u':
                vowel_count[4] = (vowel_count[4] + 1) % 2
            
            # Create a string representing the current parity state of vowels
            current_state = ''.join(map(str, vowel_count))
            
            # Check if we've seen this state before
            if current_state in state_map:
                # Calculate the length of the substring
                max_length = max(max_length, i - state_map[current_state])
            else:
                # Store the first occurrence of this state
                state_map[current_state] = i
        
        return max_length

        # Solution 2 Using XOR 
        prefixXOR = 0
        characterMap = [0] * 26
        characterMap[ord("a") - ord("a")] = 1
        characterMap[ord("e") - ord("a")] = 2
        characterMap[ord("i") - ord("a")] = 4
        characterMap[ord("o") - ord("a")] = 8
        characterMap[ord("u") - ord("a")] = 16
        mp = [-1] * 32
        longestSubstring = 0
        for i in range(len(s)):
            prefixXOR ^= characterMap[ord(s[i]) - ord("a")]
            if mp[prefixXOR] == -1 and prefixXOR != 0:
                mp[prefixXOR] = i
            longestSubstring = max(longestSubstring, i - mp[prefixXOR])
        return longestSubstring
