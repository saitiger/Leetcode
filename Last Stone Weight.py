class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            if stones[-1] == stones[-2]:
                stones.remove(stones[-2])
                stones.remove(stones[-1])
            else:
                stones[-1] = stones[-1] - stones[-2]
                stones.remove(stones[-2])
                stones = sorted(stones)
        return stones[0] if stones else 0

  # Solution 2 Using the _heappushpop_max private method breaks the max_heap function so had to use the min heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])
