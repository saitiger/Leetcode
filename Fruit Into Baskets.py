class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        i, j = 0, 0
        max_fruits = 0
        
        while j < len(fruits):
            count[fruits[j]] += 1
            
            while len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
            
            max_fruits = max(max_fruits, j - i + 1)
            
            j += 1
            
        return max_fruits
