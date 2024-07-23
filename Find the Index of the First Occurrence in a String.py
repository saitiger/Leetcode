class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1 
      
# 2 Pointer Approach
        chk = 0
        while chk < len(haystack):
            if haystack[chk] == needle[0]:
                ptr = chk
                ptr_n = 0
                while ptr < len(haystack) and ptr < len(needle) and haystack[ptr] == needle[ptr_n]:
                    ptr += 1
                    ptr_n += 1
                if ptr_n == len(needle):
                    return ptr
                else: 
                    ptr += 1
            else:
                ptr += 1
        return -1
