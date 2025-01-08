class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                s1 = words[i]
                s2 = words[j]
                # Skip if the length of the first string is longer than the second since then it can't 
                # be a prefix or suffix of the second string 
                if len(s2) < len(s1):
                    continue
                prefix = s2[:len(s1)]
                suffix = s2[-len(s1):]
                # Using Built-in function 
                # if str2.startswith(str1) and str2.endswith(str1):
                    # cnt+=1
                if prefix == s1 and suffix == s1:
                    cnt+=1
        return cnt
