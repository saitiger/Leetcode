class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen = defaultdict(int)
        for m in magazine:
            seen[m]+=1
        for r in ransomNote:
            if seen[r]==0:
                del seen[r]
            if r in seen and seen[r]>0:
                seen[r]-=1
            else:
                return False
        return True
