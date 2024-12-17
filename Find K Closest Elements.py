class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r = 0,len(arr)-k
        while l<r:
            m = (l+r)//2
            if x - arr[m]>arr[m+k] - x:
                l = m+1
            else:
                r = m
        return arr[l:l+k]

# Solution 2 Using Heap (Works on unsorted input as well)
        min_heap = [(abs(a - x), a) for a in arr]  
        heapify(min_heap)        
        res = []

        while k > 0:
            diff, element = heappop(min_heap)
            res.append(element)
            k -= 1
        return sorted(res)
