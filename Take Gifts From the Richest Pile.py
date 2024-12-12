class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxheap = [-1*g for g in gifts]
        heapq.heapify(maxheap)
        
        while k>0:
            max_val = heapq.heappop(maxheap)
            push_back = -int((-max_val)**(1/2))
            heapq.heappush(maxheap,push_back)
            k-=1
        return -sum(maxheap)
