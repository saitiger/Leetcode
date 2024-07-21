from collections import deque, defaultdict

class Solution:
    def buildMatrix(self, k, rowConditions, colConditions):
        def topoSort(edges, n):
            adj = defaultdict(list)
            indegree = [0] * (n + 1)
            order = []
            for u, v in edges:
                adj[u].append(v)
                indegree[v] += 1
            queue = deque()
            count = 0
            for i in range(1, n + 1):
                if indegree[i] == 0:
                    queue.append(i)
                    count += 1
            while queue:
                u = queue.popleft()
                order.append(u)
                for v in adj[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        queue.append(v)
                        count += 1
            if count != n:
                return []
            return order

        orderRows = topoSort(rowConditions, k)
        orderColumns = topoSort(colConditions, k)
        if not orderRows or not orderColumns:
            return []
        matrix = [[0] * k for _ in range(k)]
        positionMap = {orderColumns[i]: i for i in range(k)}
        for i in range(k):
            element = orderRows[i]
            if element in positionMap:
                matrix[i][positionMap[element]] = element
        return matrix
