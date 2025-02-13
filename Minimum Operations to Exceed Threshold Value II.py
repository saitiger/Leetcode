class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        num_ops = 0 

        while len(nums)>=2:
            minn = heapq.heappop(nums) # Smallest
            maxx = heapq.heappop(nums) # Second smallest element 

            if minn>=k: # As soon as the smallest element in the heap is equal or larger than k return 
                return num_ops

            to_push = 2*minn + maxx

            heapq.heappush(nums,to_push)
            num_ops+=1
        return num_ops
