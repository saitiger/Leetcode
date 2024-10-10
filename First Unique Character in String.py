class Solution:
    def firstUniqChar(self, s: str) -> int:
        mpp = {}

        for char in s:
            if char not in mpp:
                mpp[char] = 1
            else:
                mpp[char]+=1
        
        for i in range(len(s)):
            if mpp[s[i]]==1:
                return i
        return -1
