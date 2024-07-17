class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)
        heap = list(cnt.values())
        heapq.heapify(heap)
        res = len(heap) # Number of unique values without any removals
        while k>0 and heap:
            freq = heapq.heappop(heap)
            if freq<=k:
                k-=freq
                res-=1
        return res
# Solution 2 Count Sort
        cnt = Counter(arr)
        n = len(list(cnt.values()))
        freq = [0] * (n + 1)
        for count in cnt.values():
            freq[count] += 1
        rem = len(cnt)
        for i in range(1, n + 1):
            freq_count = min(k // i, freq[i])
            k -= (i * freq_count)
            rem -= freq_count
            if k < i:
                return rem
        return 0
