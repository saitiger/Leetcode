class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
# Solution 1 
        nums.sort()
        for i in range(len(nums)):
            if nums[i]<0 and k>0: 
                nums[i]=-nums[i]
                k-=1
            elif nums[i]==0: k=0
            else: break
        nums.sort()
        nums[0]=nums[0]*((-1)**k)
        return sum(nums)
# Solution 2
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
        while k > 0:
            minimum = heapq.heappop(heap)
            heapq.heappush(heap,-minimum)
            k -= 1
        return sum(heap)
