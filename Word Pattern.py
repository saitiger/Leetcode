class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(words)!=len(pattern):
            return False
        
        mpp = {}
        seen = set()
        for i in range(len(pattern)):
            if words[i] not in mpp and pattern[i] not in seen:
                seen.add(pattern[i])
                mpp[words[i]] = pattern[i]
            elif mpp.get(words[i]) != pattern[i]:
                return False
        return True
