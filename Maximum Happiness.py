class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        result = 0
        count = 0
        
        for i in range(k):
            result += max(happiness[i] - count, 0)
            count += 1
        
        return result
