import heapq

class Solution:
    def totalCost(self, costs, k, candidates):
        n = len(costs)
        
        pq1 = []
        pq2 = []
        
        ans = 0
        hired = 0
        i = 0
        j = n - 1
        
        while hired < k:
            while len(pq1) < candidates and i <= j:
                heapq.heappush(pq1, costs[i])
                i += 1
            while len(pq2) < candidates and j >= i:
                heapq.heappush(pq2, costs[j])
                j -= 1
            
            a = pq1[0] if pq1 else float('inf')
            b = pq2[0] if pq2 else float('inf')
            
            if a <= b:
                ans += a
                heapq.heappop(pq1)
            else:
                ans += b
                heapq.heappop(pq2)
            
            hired += 1
        
        return ans
