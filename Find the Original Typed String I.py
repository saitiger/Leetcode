class Solution:
    def possibleStringCount(self, word: str) -> int:
        freq = [0]*26

        for i in range(1,len(word)):
            if word[i]==word[i-1]:
                if freq[ord(word[i])-ord('a')]==0:
                    freq[ord(word[i])-ord('a')]+=2
                else:
                    freq[ord(word[i])-ord('a')]+=1
        
        ans = 1
        for f in freq:
            if f>0:
                ans+=(f-1)

        return ans

  # Cleaner Solution, Same Logic (Credits : Leetcode Editorial)

class Solution:
    def possibleStringCount(self, word: str) -> int:
        n, ans = len(word), 1
        for i in range(1, n):
            if word[i - 1] == word[i]:
                ans += 1
        return ans
