class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        from collections import defaultdict
        import math
        cnt = defaultdict(int)
        for x in s:
            cnt[x]+=1

        return math.floor(cnt[letter]/len(s)*100.0)
