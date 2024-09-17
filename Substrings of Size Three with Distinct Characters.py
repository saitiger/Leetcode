# Using Set 
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        
        cnt = 0
        i,j = 0,0

        while j < len(s):
            if j - i + 1 == 3:
                if len(set(s[i:j+1])) == 3:
                    cnt += 1
                i += 1
            j+=1
        return cnt

# Using Hashmap 
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        
        cnt = 0
        freq_map = {}  
        i = 0

        for j in range(len(s)):
            freq_map[s[j]] = freq_map.get(s[j], 0) + 1
            
            if j - i + 1 == 3:
                if len(freq_map) == 3:  
                    cnt += 1
                
                freq_map[s[i]] -= 1
                if freq_map[s[i]] == 0: 
                    del freq_map[s[i]]
                
                i += 1  

        return cnt

# Using Variables
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)-2):
            if(s[i]!=s[i+1] and s[i]!=s[i+2] and s[i+1]!=s[i+2]):
                count+=1
        return count
