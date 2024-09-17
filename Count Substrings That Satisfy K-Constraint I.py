class Solution:
    def countKConstraintSubstrings(self, s: str, t: int) -> int:
# Solution 1 Brute Force 
        n = len(s)
        ans = 0

        for i in range(n):
            zero_count, one_count = 0, 0
            for j in range(i, n):
                if s[j] == '0':
                    zero_count += 1
                else:
                    one_count += 1
                
                if zero_count <= t or one_count <= t:
                    ans += 1

        return ans

# Solution 2 Sliding Window 
        ans, l, ones = 0, 0, 0

        for r, n in enumerate(s):
            ones += 1 if n == '1' else 0
            while ones > k and r - l + 1 - ones > k:
                ones -= 1 if s[l] == '1' else 0
                l += 1
            ans += r - l + 1

        return ans
