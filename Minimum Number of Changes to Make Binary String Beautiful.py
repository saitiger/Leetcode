class Solution:
    def minChanges(self, s: str) -> int:
        curr = s[0]
        count = 0
        num_changes = 0
        n = len(s)

        for i in range(n):
            if s[i] == curr:
                count += 1
                continue
            if count % 2 == 0: 
                count = 1
            else:  
                count = 0
                num_changes += 1
            curr = s[i]
        return num_changes

  # Solution 2 (Credit : CodeStorywithMik)
        changes = 0
        n = len(s)
        for i in range(0, n - 1, 2):
            if s[i] != s[i + 1]:
                changes += 1
        return changes
