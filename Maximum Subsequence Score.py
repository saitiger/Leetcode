from heapq import heappush, heappop

class Solution:
    def maxScore(self, nums1, nums2, k):
        n = len(nums1)
        
        arr = [(nums1[i], nums2[i]) for i in range(n)]
        
        arr.sort(key=lambda x: x[1], reverse=True)
        
        min_heap = [] 
        
        Ksum = 0
        
        for i in range(k):
            Ksum += arr[i][0]
            heappush(min_heap, arr[i][0])
        
        result = Ksum * arr[k-1][1]
        
        for i in range(k, n):
            Ksum += arr[i][0] - heappop(min_heap)
            heappush(min_heap, arr[i][0])
            result = max(result, Ksum * arr[i][1])
        
        return result
