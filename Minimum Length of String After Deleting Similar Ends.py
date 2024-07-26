class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        if(s[l]!=s[r]):
            return len(s)
        while l < r and s[l] == s[r]:
            tmp = s[l]
            while l <= r and s[l] == tmp:
                l += 1
            while l <= r and s[r] == tmp:
                r -= 1
        return r - l + 1
