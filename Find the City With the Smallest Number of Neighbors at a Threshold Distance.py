import heapq
from collections import defaultdict

class Solution:
    def dijkstra(self, n, adj, result, S):
        pq = []
        heapq.heappush(pq, (0, S))
        result[S] = 0
        while pq:
            d, node = heapq.heappop(pq)
            if d > result[node]:
                continue
            for adjNode, dist in adj[node]:
                if d + dist < result[adjNode]:
                    result[adjNode] = d + dist
                    heapq.heappush(pq, (d + dist, adjNode))

    def getCityWithFewestReachable(self, n, shortestPathMatrix, distanceThreshold):
        cityWithFewestReachable = -1
        fewestReachableCount = float('inf')
        for i in range(n):
            reachableCount = 0
            for j in range(n):
                if i != j and shortestPathMatrix[i][j] <= distanceThreshold:
                    reachableCount += 1
            if reachableCount <= fewestReachableCount:
                fewestReachableCount = reachableCount
                cityWithFewestReachable = i
        return cityWithFewestReachable

    def findTheCity(self, n, edges, distanceThreshold):
        adj = defaultdict(list)
        shortestPathMatrix = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            shortestPathMatrix[i][i] = 0
        for start, end, weight in edges:
            adj[start].append((end, weight))
            adj[end].append((start, weight))
        for i in range(n):
            self.dijkstra(n, adj, shortestPathMatrix[i], i)
        return self.getCityWithFewestReachable(n, shortestPathMatrix, distanceThreshold)
