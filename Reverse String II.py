class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)  
        n = len(s)
        # Reverse from i to i+k for each chunk of 2*k characters
        for i in range(0, n, 2 * k):
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)

# Without converting to List
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        n = len(s)
        # Work on chunks of 2*k characters
        for i in range(0, n, 2 * k):
            first_k = s[i:i + k][::-1]      # Reverse first k
            second_k = s[i + k:i + 2 * k]   # Don't change the next k characters
            result += first_k + second_k
        return result
