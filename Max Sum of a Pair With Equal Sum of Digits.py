# Solution 1 
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum = defaultdict(list)

        for n in nums:
            s = 0  
            num_copy = n
            while num_copy:
                s += num_copy % 10
                num_copy = num_copy // 10
            digit_sum[s].append(n)  
      
        max_sum = float('-inf')
      
        for v in digit_sum.values():
            if len(v) > 1:
                v.sort(reverse=True) 
                max_sum = max(max_sum, v[0] + v[1])  # Take the two largest numbers
        return max_sum if max_sum != float('-inf') else -1

# Solution 2 
class Solution:
    def maximumSum(self, nums):
        digit_sum = [[] for _ in range(82)]
        max_sum = -1
      
        for n in nums:
            s = 0
            num_copy = n
            while num_copy:
              s+=n%10
              num_copy=num_copy//10
            heapq.heappush(digit_sum_groups[num_copy],n)

            if len(digit_sum[s]) > 2:
                heapq.heappop(digit_sum_groups[s])
              
        for min_heap in digit_sum:
            if len(min_heap) == 2:
                first = heapq.heappop(min_heap)
                second = heapq.heappop(min_heap)
                max_sum = max(max_sum, first + second)
        return max_sum
