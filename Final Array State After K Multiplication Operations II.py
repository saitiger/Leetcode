# The fundamental idea is to detect the cycle i.e. after a point we reach the same state/ have a cycle post which the order in which the multiplier 
# is applied. So we complete the cycle find the value and then multiply it y number of times into the number of cycles. Remaining elements once the cycle is 
# complete are multiplied in the original order of the cycle.

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums
        
        n = len(nums)
        mod = int(10**9) + 7
        min_heap = [(val, idx) for idx,val in enumerate(nums)]
        heapify(min_heap)
        max_val = max(nums)
        
        while k:
            x, i = heappop(min_heap)
            nums[i] = x * multiplier
            heappush(min_heap, (nums[i], i))
            k -= 1
            
            if x > max_val:
                break
        
        rem = k % n
        k = k // n
        
        for i in range(rem):
            x, i = heappop(min_heap)
            nums[i] = (x * multiplier) % mod
        
        mpow = pow(multiplier, k, mod)
        for i in range(n):
            nums[i] = (nums[i] * mpow) % mod
        
        return nums
