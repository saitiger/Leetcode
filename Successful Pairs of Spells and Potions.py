class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions.sort()
        n = len(potions)

        for x in spells:
            l = 0
            r  = len(potions) - 1
            
            while l <= r:
                m = l + ((r - l) // 2)
                if x * potions[m] >= success:
                    r = m - 1
                else:
                    l = m + 1
            if l < len(potions):
                ans.append(n - l)
            else:
                ans.append(0)
        return ans
