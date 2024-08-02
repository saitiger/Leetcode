class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()

        for c in s:
            if c in seen:
                return c 
            else:
                seen.add(c)
