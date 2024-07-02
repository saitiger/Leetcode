class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    # Solution 1
        d = []
        for x, y in points:
            dist = ((x ** 2) + (y ** 2))**0.5
            d.append([x,y,dist])
        d.sort(key = lambda x : x[2])
        return [x[:2] for x in d][:k]      
      # Solution 2 
      minHeap = []
        for x, y in points:
            dist = ((x ** 2) + (y ** 2))**0.5
            minHeap.append((dist, x, y))
        heapq.heapify(minHeap)
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append((x, y))
        return res
