class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev,result = 0,0
        n = len(target)
        for i in range(n):
            curr = target[i]
            if(prev<curr):
                result+=curr-prev
            prev = curr
        return result
