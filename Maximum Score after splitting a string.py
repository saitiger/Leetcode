class Solution:
    def maxScore(self, s: str) -> int:
        # Brute Force
        ans = 0
        for i in range(len(s) - 1):
            curr = 0
            for j in range(i + 1):
                if s[j] == "0":
                    curr += 1
            for j in range(i + 1, len(s)):
                if s[j] == "1":
                    curr += 1
            ans = max(ans, curr)
        return ans

# Solution 2 Counting One's and Zero's        
        ones = s.count("1")
        zeros = 0
        ans = 0 
        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
            ans = max(ans, zeros + ones)
        return ans
