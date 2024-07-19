# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         maxLength = 0
#         charMap = {}
#         left = 0
#         for right in range(n):
#             if s[right] not in charMap or charMap[s[right]] < left:
#                 charMap[s[right]] = right
#                 maxLength = max(maxLength, right - left + 1)
#             else:
#                 left = charMap[s[right]] + 1
#                 charMap[s[right]] = right
#         return maxLength

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
