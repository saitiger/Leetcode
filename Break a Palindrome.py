class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        
        st = [s for s in palindrome]
        
        for i in range(n // 2):
            if st[i] != 'a':
                st[i] = 'a'
                return ''.join(st)
        
        st[-1] = 'b'
        return ''.join(st)
