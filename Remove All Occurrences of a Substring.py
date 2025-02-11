# Solution 1 
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            idx = s.find(part)
            s = s[:idx] + s[idx + len(part) :]
        return s

# Solution 2 
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stk = []
        part_len = len(part)
        for char in s:
            stk.append(char)
            if len(stk) >= part_len and "".join(stk[-part_len:]) == part: 
                # Stack stores in the reverse order so need to traverse the string part in reverse
                del stk[-part_len:] 
        return "".join(stk)
