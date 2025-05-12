class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = []
        mp = [0] * 10
        
        for digit in digits:
            mp[digit] += 1
        
        # First digit : Cannot be zero
        for i in range(1, 10):
            if mp[i] == 0:
                continue
            mp[i] -= 1
            
            for j in range(10):
                if mp[j] == 0:
                    continue
                mp[j] -= 1
                
                for k in range(0, 10, 2):
                    if mp[k] == 0:
                        continue
                    mp[k] -= 1
                    
                    num = i * 100 + j * 10 + k
                    result.append(num)
                    mp[k] += 1
                mp[j] += 1            
            mp[i] += 1
        
        return result
