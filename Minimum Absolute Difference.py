class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        diff = float('inf')

        for i in range(1, len(arr)):
            cur = arr[i]-arr[i-1]
            if cur== diff:
                res.append([arr[i-1], arr[i]])
            elif cur < diff:
                diff = cur
                res = [[arr[i-1], arr[i]]]
        return res
        
