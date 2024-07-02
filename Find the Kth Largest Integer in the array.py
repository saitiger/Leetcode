class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        max_heap = [int(n) for n in nums]
        heapq._heapify_max(max_heap)
        while k>1:
            heapq._heappop_max(max_heap)
            k-=1
        return str(max_heap[0])
