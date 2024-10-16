class Solution:
    def partitionString(self, s: str) -> int:
        cnt =  1
        seen = set()
        for char in s:
            if char not in seen:
                seen.add(char)
                # print(seen)
            else:
                seen = set()
                seen.add(char)
                cnt+=1
        return cnt

# Solution 2 
class Solution:
    def partitionString(self, s: str) -> int:
        last_seen = [-1] * 26
        
        count = 0
        substring_start = 0

        for i in range(len(s)):
            if last_seen[ord(s[i]) - ord('a')] >= substring_start:
                count += 1
                substring_start = i
            last_seen[ord(s[i]) - ord('a')] = i

        return count + 1
