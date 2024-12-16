class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = [(n,idx) for idx,n in enumerate(nums)]
        heapq.heapify(min_heap)
        while k:
            _,idx = heapq.heappop(min_heap)
            nums[idx] *= multiplier
            heapq.heappush(min_heap,(nums[idx],idx))
            k-=1
        return nums 
