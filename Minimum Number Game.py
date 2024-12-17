# Solution 1 
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 1
        while i<len(nums):
            nums[i-1],nums[i] = nums[i],nums[i-1]
            i+=2
        return nums           

# Solution 2 Using Heap
        heapq.heapify(nums)
        res = []
        while nums:
            alice = heapq.heappop(nums)
            bob = heapq.heappop(nums)
            res.append(bob)
            res.append(alice)
        return res
