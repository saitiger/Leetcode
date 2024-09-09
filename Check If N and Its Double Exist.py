# Solution 1 
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        zero_count = 0
        for a in arr:
            seen.add(a)
            if a == 0:
                zero_count += 1
                
        if zero_count > 1:
            return True

        for s in seen:
            if s!=0 and s*2 in seen:
                return True
            else:
                continue 
        return False

# Solution 2 
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for x in arr:
            if 2*x in seen or x/2 in seen: return True
            seen.add(x)
        return False 
