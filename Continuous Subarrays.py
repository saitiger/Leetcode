class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        min_heap = []  
        max_heap = []  
        left = right = 0
        count = 0

        while right < len(nums):
            heapq.heappush(min_heap, (nums[right], right))
            heapq.heappush(max_heap, (-nums[right], right))

            while left < right and -max_heap[0][0] - min_heap[0][0] > 2:
                left += 1

                while min_heap and min_heap[0][1] < left:
                    heapq.heappop(min_heap)
                while max_heap and max_heap[0][1] < left:
                    heapq.heappop(max_heap)

            count += right - left + 1
            right += 1

        return count
