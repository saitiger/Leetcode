class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res

# Solution 2 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        srt = sorted(strs)
        first = srt[0]
        last = srt[-1]

        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return res
            res = res + first[i]
        return res
