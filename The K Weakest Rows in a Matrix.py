class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        min_heap = []
        for r in range(rows):
            row_sum = 0  # Finding the sum of each row
            for c in range(cols):
                if mat[r][c]==1:
                    row_sum+=1
                else:
                    break  # Stop counting when we hit first 0
            heapq.heappush(min_heap, (row_sum,r)) 
            # Add each row's count and index (Outside the else inner loop to ensure the case when all 1's occur it is counted)

        res = []
        while k:
            val,idx = heapq.heappop(min_heap)
            res.append(idx)
            k-=1
        return res
