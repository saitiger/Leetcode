class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(queries)):
            k,t = queries[i]
            heap = []
            for j in range(len(nums)):
                heap.append(( nums[j][-t:],j))
            heapq.heapify(heap)
            temp = 0
            for _ in range(k):
                temp = heapq.heappop(heap)[1]
            ans.append(temp)
        return ans            
