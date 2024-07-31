import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        m = len(nums1)
        n = len(nums2)
        pq = []
        
        visited = set()
        visited.add((0, 0))
        
        sum_val = nums1[0] + nums2[0]
        
        heapq.heappush(pq, (sum_val, 0, 0))
        
        result = []
        while k > 0 and pq:
            
            temp = heapq.heappop(pq)
            
            i, j = temp[1], temp[2]
            result.append([nums1[i], nums2[j]])
            
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(pq, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            
            k -= 1
        
        return result
