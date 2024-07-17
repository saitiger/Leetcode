class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        i = 0
        removed = set()
        for j in range(len(nums) // 2, len(nums)):
            if nums[j] > nums[i] and i not in removed:
                removed.add(i)
                removed.add(j)
                i += 1
        return len(nums) - len(removed)
# Solution 2 Using Heap
        counts = [-x for x in Counter(nums).values()]
        heapq.heapify(counts)
        while len(counts) > 1:
            a = -heapq.heappop(counts)
            b = -heapq.heappop(counts)
            if a > 1:
                heapq.heappush(counts, -a + 1)
            if b > 1:
                heapq.heappush(counts, -b + 1)
        return -sum(counts)
