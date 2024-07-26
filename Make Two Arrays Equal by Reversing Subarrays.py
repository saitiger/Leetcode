class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        res = [0] * 1001
        n = len(target)
        for i in range(n):
            res[target[i]] += 1
            res[arr[i]] -= 1
        
        for i in range(1001):
            if res[i]:
                return False
        return True

        # Solution 2
        target.sort() 
        arr.sort() 
        return True if arr == target else False
