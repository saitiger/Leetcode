class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        max_len, ans = 0, ""
        len_s = len(s)
        for start in range(len_s - 1):
            if len_s - start < max_len:
                break
            lower_set = set()
            upper_set = set()
            for end in range(start, len_s):
                if s[end].islower():
                    lower_set.add(s[end])
                else:
                    upper_set.add(s[end].lower())
                if lower_set == upper_set:
                    if end - start + 1 > max_len:
                        ans = s[start: end + 1]
                        max_len = end - start + 1
        return ans
